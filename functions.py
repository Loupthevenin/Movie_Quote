import requests
from bs4 import BeautifulSoup
import math

from settings import *


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


# Determine des listes de citations, personnages, ids
def list_all(id_number_movie, page_number):
    soups = html_soup(url_movie, ids_movie[id_number_movie], page_number)
    block_links = soups.find_all("blockquote")
    for block_link in block_links:
        tag_quote = block_link.find("a")
        tag_character = block_link.find("footer")
        quote_list.append(tag_quote.get_text())
        character_list.append(tag_character.get_text())
        ids_list.append(ids_movie[id_number_movie])
