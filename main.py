from pprint import pprint
import re

from functions import *

character_str = ""
FILTRE = (r'\d+\s*\(\d+\s*votes?\)|\d+.|TagsTopsLiensPartenariatDernièresSagasPersonnagesÀ '
          r'proposMosaïqueProposerMentions légales|Saga|Traduction')

if __name__ == '__main__':

    for id_movie in range(0, len(ids_movie)):
        number_page = find_number_pages(ids_movie[id_movie])
        if number_page == 1:
            list_quote(id_movie, number_page)
            list_character(id_movie, number_page)
        elif number_page > 1:
            for i in range(1, number_page + 1):
                number_page = i
                list_quote(id_movie, number_page)
                list_character(id_movie, number_page)
        else:
            print("Probleme")

    quote_list_clean = [item for item in quote_list if "Traduction" not in item]
    character_str = " ".join(character_list)
    character_str = re.sub(FILTRE, '', character_str)
    character_list_clean = [element.strip() for element in character_str.split('.') if element.strip()]

    pprint(quote_list_clean)
    pprint(character_list_clean)
    print(len(quote_list_clean))
    print(len(character_list_clean))
