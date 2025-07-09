import argparse
import csv
from typing import List, Dict
from pubmed_fetcher.fetch import fetch_pubmed_ids, fetch_paper_details


def write_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    if not data:
        print("No data to write.")
        return
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-f", "--file", type=str, help="CSV output file name")
    parser.add_argument("-d",
                        "--debug",
                        action="store_true",
                        help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"Query: {args.query}")

    try:
        ids = fetch_pubmed_ids(args.query)
        if args.debug:
            print(f"Found {len(ids)} PubMed IDs.")

        papers = fetch_paper_details(ids)

        if args.file:
            write_to_csv(papers, args.file)
            print(f"✅ Results saved to {args.file}")
        else:
            for paper in papers:
                print(paper)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
