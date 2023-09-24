import requests
from bs4 import BeautifulSoup
import math

url_movie = "https://www.kaakook.fr/film-"  # 20 citations par page

ids_movie = [29, 67, 68, 1691]  # matrix, matrix 2, matrix 3, inception+

quote_list = []  # liste de toutes les citations
character_list = []  # liste de tout les personnages de chaque citation


def html_soup(url, ids, pages):
    if ids and pages:
        html_pages = requests.get(f"{url}{ids}-{pages}")
        if html_pages.status_code != 404 or html_pages.status_code != 410:
            soup = BeautifulSoup(html_pages.text, 'html.parser')
            return soup
        else:
            return "ERROR"
    elif not ids:
        html = requests.get(url)
        if html.status_code != 404 or html.status_code != 410:
            soup = BeautifulSoup(html.text, 'html.parser')
            return soup
        else:
            return "ERROR"


def find_tag_dd(soup, number_of_dd):
    dl_tag = soup.find('dl')
    if dl_tag:
        dd_tags = dl_tag.find_all('dd')
        if len(dd_tags) >= number_of_dd:
            result = dd_tags[number_of_dd - 1].get_text()
            if result.isdigit():
                return int(result)
            else:
                return str(result)
        else:
            print("Il n'y pas assez de balises <dd> à l'interieur de la balise <dl>.")  # a modifier
    else:
        print("La balise <dl> n'a pas été trouvée.")  # a modifier


def find_number_pages(id_number) -> int:
    soups = html_soup(url_movie, id_number, 1)
    number_quote = find_tag_dd(soups, 4)
    return math.ceil(number_quote/20)


# Determine une liste de toutes les citations
def list_quote(id_number_movie, page_number):
    soups = html_soup(url_movie, ids_movie[id_number_movie], page_number)
    quote_links = soups.find_all('a', href=lambda href: href and '/citation-' in href)
    for link in quote_links:
        quote_list.append(link.text)


# Determine une liste de tout les personnages
def list_character(id_number_movie, page_number):
    soups = html_soup(url_movie, ids_movie[id_number_movie], page_number)
    character_links = soups.find_all('footer')
    for link in character_links:
        character_list.append(link.text)
