PubMed Fetcher:
A command-line tool to search PubMed for research papers with non-academic authors (from companies, biotech firms, pharmaceutical companies, etc.).

Features
Search PubMed database using custom queries
Filter results to show only papers with non-academic authors
Extract author affiliations and company information
Export results to CSV format
Debug mode for detailed search information
Installation
This project runs on Python 3.11+ and uses the following dependencies:

requests - for API calls to PubMed
Built-in libraries: argparse, csv, xml.etree.ElementTree
Usage
Basic Search
python cli.py "your search query"
Save Results to CSV
python cli.py "cancer immunotherapy" -f results.csv
Enable Debug Mode
python cli.py "machine learning" -d
Combined Options
python cli.py "COVID-19 treatment" -f covid_results.csv -d
Command Line Arguments
query (required): PubMed search query string
-f, --file: CSV output file name
-d, --debug: Enable debug mode to see search progress
Example Queries
"cancer immunotherapy" - Find papers about cancer immunotherapy
"CAR-T cell therapy" - Search for CAR-T cell research
"checkpoint inhibitors cancer" - Look for immune checkpoint inhibitor studies
"mRNA vaccine" - Find mRNA vaccine research
Output Format
The tool generates CSV files with the following columns:

PubmedID: Unique PubMed identifier
Title: Paper title
Publication Date: Date of publication
Non-academic Author(s): Names of authors from non-academic institutions
Company Affiliation(s): Company or organization affiliations
Corresponding Author Email: Contact email (when available)
How It Works
Search: Queries the PubMed database using NCBI's E-utilities API
Filter: Identifies papers with authors from non-academic institutions
Extract: Pulls relevant information (title, authors, affiliations, emails)
Export: Saves filtered results to CSV format
Non-Academic Institution Detection
The tool identifies non-academic affiliations using keywords such as:

Company identifiers: "inc", "ltd", "corp", "llc", "gmbh"
Industry terms: "pharma", "biotech", "r&d", "laboratories"
Major pharmaceutical companies: "novartis", "pfizer", "astrazeneca", "roche", "merck"
Project Structure
pubmed-fetcher/
├── pubmed_fetcher/
│   ├── __init__.py
│   ├── fetch.py          # Core PubMed API functions
│   └── utils.py          # Utility functions for email/affiliation detection
├── cli.py                # Command-line interface
├── main.py               # Entry point
├── pyproject.toml        # Project configuration
└── README.md             # This file
API Rate Limits
This tool uses NCBI's E-utilities API, which has usage guidelines:

No more than 3 requests per second
The tool fetches up to 100 papers per search by default
License
This project is open source and available under standard terms.

Author
Created by Assistant

Contributing
Feel free to submit issues or pull requests to improve the tool's functionality or add new features.