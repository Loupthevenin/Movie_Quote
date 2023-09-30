import json
import re

from functions import *
from settings import *


if __name__ == '__main__':

    # on vérifie si le fichier json existe et on le crée sinon
    if not os.path.exists(path):
        with open(path, 'w') as file_json:
            json.dump({}, file_json)

    # On stock notre base de donnée dans une variable
    with open(path, 'r', encoding="utf-8") as data_json:
        data = json.load(data_json)

    # On vérifie si notre fichier json contient deja nos films et on modifie la liste en fonction
    if base_data.keys() == data.keys() and data["ids"]:
        remove_list = list(set(data['ids']))
        for value_remove in remove_list:
            if value_remove in ids_movie:
                ids_movie.remove(value_remove)
    elif base_data.keys() != data.keys():
        print('yes')
        data = base_data

    # On exécute le code qui va scrap toutes les citations de films/perso qui n'est pas encore dans le fichier json
    for id_movie in range(0, len(ids_movie)):
        number_page = find_number_pages(ids_movie[id_movie])
        if number_page == 1:
            list_quote_ids(id_movie, number_page)
            list_character(id_movie, number_page)
        elif number_page > 1:
            for i in range(1, number_page + 1):
                number_page = i
                list_quote_ids(id_movie, number_page)
                list_character(id_movie, number_page)
        else:
            print("Probleme")

    if len(ids_movie) > 0:
        data["ids"] = [item for item in data["ids"] + ids_list]
        data["quotes"] = [item for item in data["quotes"] + quote_list if "Traduction" not in item]

        character_str = " ".join(character_list)
        character_str = re.sub(FILTRE, '', character_str)
        for element in FILTRE_syntax:
            if element in character_str:
                character_str = character_str.replace(element, "Dr")
        data["character"] = [element.strip() for element in data["character"] + character_str.split('.') if element.strip()]

        # DATA tri
        data = {key: [value for _, value in sorted(zip(data["ids"], values))] for key, values in data.items()}

        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(len(data["quotes"]))
        print(len(data["character"]))
        print(len(data["ids"]))
    elif len(ids_movie) == 0:
        print("Les données sont déjà sauvegardé.")
        print(len(data["quotes"]))
        print(len(data["character"]))
        print(len(data["ids"]))
