import requests
from bs4 import BeautifulSoup

url_movie = "https://www.kaakook.fr/film-"  # 20 citations par page

ids_movie = [29, 67, 68, 1691]  # matrix, matrix 2, matrix 3, inception+

quote_list = []  # liste de toutes les citations
character_list = []  # liste de tout les personnages de chaque citation


def find_number_pages(id_number) -> int:
    html_find = requests.get(f"{url_movie}{id_number}")
    soup_find = BeautifulSoup(html_find.text, 'html.parser')
    dl_tag = soup_find.find('dl')
    if dl_tag:
        dd_tags = dl_tag.find_all('dd')
        if len(dd_tags) >= 4:
            number_quote = int(dd_tags[3].get_text())
            return find_number_boucle(analyse_number=number_quote)
        else:
            print("Il n'y pas assez de balises <dd> à l'interieur de la balise <dl>.")  # a modifier
    else:
        print("La balise <dl> n'a pas été trouvée.")  # a modifier


# Trouve le nombre de page a l'aide du nombre de citation
def find_number_boucle(analyse_number) -> int:
    seuils = [160, 140, 120, 100, 80, 60, 40, 20]
    valeurs = [9, 8, 7, 6, 5, 4, 3, 2]

    for seuil, valeur in zip(seuils, valeurs):
        if analyse_number > seuil:
            return valeur

    return 1


def list_quote(id_number_movie, page_number):
    html_pages = requests.get(f"{url_movie}{ids_movie[id_number_movie]}-{page_number}")
    soup = BeautifulSoup(html_pages.text, 'html.parser')
    quote_links = soup.find_all('a', href=lambda href: href and '/citation-' in href)
    for link in quote_links:
        quote_list.append(link.text)


def list_character(id_number_movie, page_number):
    html_pages = requests.get(f"{url_movie}{ids_movie[id_number_movie]}-{page_number}")
    soup = BeautifulSoup(html_pages.text, 'html.parser')
    # character_links = soup.find_all('a', href=lambda href: href and '/perso-' in href)
    character_links = soup.find_all('footer')
    for link in character_links:
        character_list.append(link.text)