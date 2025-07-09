import requests
import xml.etree.ElementTree as ET
from typing import List, Dict
from pubmed_fetcher.utils import extract_email, is_non_academic_affiliation

BASE_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
BASE_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_pubmed_ids(query: str, retmax: int = 100) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax
    }
    response = requests.get(BASE_ESEARCH, params=params)
    response.raise_for_status()
    data = response.json()
    return data["esearchresult"]["idlist"]


def fetch_paper_details(pubmed_ids: List[str]) -> List[Dict[str, str]]:
    if not pubmed_ids:
        return []

    params = {"db": "pubmed", "id": ",".join(pubmed_ids), "retmode": "xml"}
    response = requests.get(BASE_EFETCH, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or ""
        title = article.findtext(".//ArticleTitle") or ""
        pub_date_node = article.find(".//PubDate")
        pub_date = "".join([
            pub_date_node.findtext(part) or ''
            for part in ["Year", "Month", "Day"]
        ]) if pub_date_node else ""

        authors = article.findall(".//Author")
        non_academic_authors = []
        companies = set()
        email = ""

        for author in authors:
            aff = author.findtext("AffiliationInfo/Affiliation") or ""
            if not email:
                extracted_email = extract_email(aff)
                if extracted_email:
                    email = extracted_email
            if is_non_academic_affiliation(aff):
                name = "{} {}".format(
                    author.findtext("ForeName") or "",
                    author.findtext("LastName") or "").strip()
                if name:
                    non_academic_authors.append(name)
                companies.add(aff)

        if non_academic_authors:
            results.append({
                "PubmedID":
                pmid,
                "Title":
                title,
                "Publication Date":
                pub_date,
                "Non-academic Author(s)":
                "; ".join(non_academic_authors),
                "Company Affiliation(s)":
                "; ".join(companies),
                "Corresponding Author Email":
                email
            })

    return results
