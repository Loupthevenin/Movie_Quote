import json
import re

from functions import *
from settings import *


def main():
    # On clear les listes
    quote_list.clear()
    ids_list.clear()
    character_list.clear()

    # on vérifie si le fichier json existe et on le crée sinon
    if not os.path.exists(path_quote):
        with open(path_quote, 'w') as file_json:
            json.dump({}, file_json)

    # On stock notre base de donnée dans une variable
    with open(path_quote, 'r', encoding="utf-8") as data_json:
        data = json.load(data_json)

    # On vérifie s'il y a des films à retirer
    if remove_ids_list:
        remove_index = []
        for num, line in enumerate(data["ids"]):
            if line in remove_ids_list:
                remove_index.append(num)
        for remove_value in reversed(remove_index):
            del data["ids"][remove_value]
            del data["quotes"][remove_value]
            del data["character"][remove_value]

    # On vérifie si notre fichier json contient deja nos films et on modifie la liste en fonction
    if base_data.keys() == data.keys() and data["ids"]:
        remove_list = list(set(data['ids']))
        for value_remove in remove_list:
            if value_remove in ids_movie:
                ids_movie.remove(value_remove)
    elif base_data.keys() != data.keys():
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
        data["ids"].extend(ids_list)
        data["quotes"].extend([item for item in quote_list if "Traduction" not in item])

        character_str = " ".join(character_list)
        character_str = re.sub(FILTRE, '', character_str)
        for element in FILTRE_syntax:
            if element in character_str:
                character_str = character_str.replace(element, "Dr")
        data["character"].extend([element.strip() for element in character_str.split('.') if element.strip()])

        # DATA tri
        data = {key: [value for _, value in sorted(zip(data["ids"], values))] for key, values in data.items()}

        with open(path_quote, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    elif len(ids_movie) == 0:
        with open(path_quote, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    # On vérifie les données
    if len(data["quotes"]) == len(data["character"]) == len(data["ids"]):
        print("Données sauvegardés !")
    else:
        print(f"Actualiser le filtre en consequence :")
        print(f"Quotes : {len(data['quotes'])}")
        print(f"character : {len(data['character'])}")
        print(f"Ids : {len(data['ids'])}")


if __name__ == '__main__':
    main()
