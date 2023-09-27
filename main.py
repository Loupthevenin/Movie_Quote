import json
import os
import re

from functions import *

FILTRE = (r"\d+\s*\(\d+\s*votes?\)|\d+.|TagsTopsLiensPartenariatDernièresSagasPersonnagesÀ "
          r"proposMosaïqueProposerMentions légales|TagsTopsLiensPartenariatDernièresSagasPersoÀ "
          r"proposMosaïqueProposerMentions légales"
          r"|Saga|Traduction")
FILTRE_syntax = ["Dr."]
path = os.path.join(os.path.dirname(__file__), 'data/data_quote.json')
base_data = {"ids": [],
             "quotes": [],
             "character": []
             }
encode = 0


def update_database(data_script, data_file_json, _encode):
    # Si json vide
    if _encode == 0:
        data_script["ids"] = [item for item in ids_list]
        data_script["quotes"] = [item for item in quote_list if "Traduction" not in item]

        character_str = " ".join(character_list)
        character_str = re.sub(FILTRE, '', character_str)
        for element in FILTRE_syntax:
            if element in character_str:
                character_str = character_str.replace(element, "Dr")
        data_script["character"] = [element.strip() for element in character_str.split('.') if element.strip()]

        with open(path, 'w', encoding="utf-8") as f:
            json.dump(base_data, f, ensure_ascii=False, indent=4)

        print(len(data_script["quotes"]))
        print(len(data_script["character"]))
        print(len(data_script["ids"]))

    # Si json contient des données
    elif _encode == 1:
        data_file_json["ids"] = [item for item in data_file_json["ids"] + ids_list]
        data_file_json["quotes"] = [item for item in data_file_json["quotes"] + quote_list if "Traduction" not in item]

        character_str = " ".join(character_list)
        character_str = re.sub(FILTRE, '', character_str)
        for element in FILTRE_syntax:
            if element in character_str:
                character_str = character_str.replace(element, "Dr")
        data_file_json["character"] = [element.strip() for element in data_file_json["character"] + character_str.split('.') if element.strip()]

        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(len(data_file_json["quotes"]))
        print(len(data_file_json["character"]))
        print(len(data_file_json["ids"]))


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
        encode = 1
        remove_list = list(set(data['ids']))
        for value_remove in remove_list:
            if value_remove in ids_movie:
                ids_movie.remove(value_remove)

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

    if encode == 0:
        update_database(base_data, data, encode)
    elif encode == 1:
        update_database(base_data, data, encode)
    else:
        print("Tout est deja sauvegardé")


"""Modifier le code def update dans le if des fonctions au fait deux fois le boulot !!! ids_list"""
