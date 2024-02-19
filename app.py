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

    try:
        response = requests.get(url, timeout=(3, 5))
        soup = BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.Timeout:
        sys.exit("The request timed out")
    except requests.exceptions.RequestException as e:
        sys.exit("An error occurred:", e)

    article_details = get_article_details(soup, url)

    reference = get_reference(domain, article_details)

    print(reference)


def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain


def get_article_details(soup, url):
    # Title
    title = soup.find(class_='article-title').get_text()

    # Author & date
    author_and_date_div = soup.find('div', class_='author-and-date')
    author = author_and_date_div.find('strong').get_text()
    date = author_and_date_div.get_text().split('-')[-1].strip()
    rating = None

    if soup.find('section', class_='block-hero-category-arvostelut'):
        # Rating
        rating_div = soup.find(class_='rating')
        one_count = len(rating_div.find_all(class_='one'))
        half_count = len(rating_div.find_all(class_='half'))
        rating = one_count + 0.5 * half_count

    article_details = {
        "title": title,
        "date": date,
        "author": author,
        "url": url,
        "rating": rating if rating else None
    }

    return article_details


def get_reference(domain, article_details):
    current_date = datetime.now().strftime("%d.%m.%Y")
    # Remove leading zeros from day and month
    current_date = current_date.replace('.0', '.').lstrip('0')

    date = f"Ajankohta = {article_details['date']}"

    if article_details['rating']:
        site = domain.split('.')[0].title()
        review = f"* [[{site}]]: {{{{Arvostelutähdet|{article_details['rating']}|5}}}}"

    reference = (f"<ref>{{{{Verkkoviite | Osoite = {article_details['url']} | Nimeke = {article_details['title']}"
                 f" | Tekijä = {article_details['author']} | Sivusto = {domain} | "
                 f"{date} | Viitattu = {current_date} }}}}</ref>")

    return review + reference if article_details['rating'] else reference


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Käyttö: python app.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    main(url)
