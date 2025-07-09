from typing import Optional


def extract_email(affiliation: str) -> Optional[str]:
    if "@" in affiliation:
        # Very basic heuristic
        start = affiliation.find("@") - 1
        while start >= 0 and affiliation[start].isalpha():
            start -= 1
        return affiliation[start + 1:].split()[0]
    return None


def is_non_academic_affiliation(affiliation: str) -> bool:
    """
    Heuristic to detect if affiliation is non-academic.
    """
    non_academic_keywords = [
        "inc", "ltd", "gmbh", "pharma", "biotech", "corp", "company", "r&d",
        "llc", "ag", "ab", "industries", "laboratories", "solutions",
        "novartis", "pfizer", "astrazeneca", "roche", "merck"
    ]
    return any(keyword in affiliation.lower()
               for keyword in non_academic_keywords)
