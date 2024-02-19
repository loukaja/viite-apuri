from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urlparse
from datetime import datetime

SUPPORTED_DOMAINS = ['kaaoszine.fi']


def main(url):
    domain = get_domain(url)

    if domain not in SUPPORTED_DOMAINS:
        print("Tuntematon domain, luo viite manuaalisesti")
        sys.exit(1)
    
    if is_review_url(url):
        get_review_details(url)

    reference = get_reference(url)


def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain


def is_review_url(url):
    return False

def get_review_details(url)
    return None

def get_reference(url):
    pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Käyttö: python app.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    main(url)
