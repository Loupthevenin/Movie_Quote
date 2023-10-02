import json

from settings import *


class Database:
    @staticmethod
    def load_json(path, read_write, var_dump=None):
        if read_write == "r":
            with open(path, "r", encoding='utf-8') as f:
                return json.load(f)
        elif read_write == "w":
            with open(path, "w", encoding='utf-8') as f:
                return json.dump(var_dump, f)
        else:
            print("ERROR LOAD JSON")

    def search(self, text: str):
        resultat = []
        if isinstance(text, str):
            data_movie = self.load_json(path_movie, "r")
            for num, line in enumerate(data_movie['title_movies']):
                if text.lower() in line.lower():
                    resultat.append(f"{line}\t[ID]: {data_movie['id_movies'][num]} :[ID]\t[TYPE]: {data_movie['type_movie'][num]} :[TYPE]")
        else:
            print("Ce n'est pas du texte !!!")
        if resultat:
            print('-'*50)
            print(f"Nombre de films trouvés : {len(resultat)}\n")
            [print(element) for element in resultat]
        else:
            print("Aucun film correspondant")

    def search_num_quotes(self, number_quotes="", types="Film Série", top=0):
        resultat = []
        data_movie = self.load_json(path_movie, "r")
        if isinstance(number_quotes, int):
            for num, line in enumerate(data_movie['number_quotes']):
                if number_quotes < line and data_movie['type_movie'][num] in types:
                    resultat.append(f"{line}\t[TITLE]: {data_movie['title_movies'][num]} :[TITLE]\t[ID]: {data_movie['id_movies'][num]} :[ID]")
            if resultat:
                print('-' * 50)
                print(f"Nombre de films trouvés : {len(resultat)}\n")
                resultat = sorted(resultat, key=lambda x: int(x.split()[0]), reverse=True)
                [print(element) for element in resultat]
            else:
                print("Aucun film correspondant")
        elif top != 0:
            for num, line in enumerate(data_movie['number_quotes']):
                if data_movie['type_movie'][num] in types:
                    resultat.append(f"{line}\t[TITLE]: {data_movie['title_movies'][num]} :[TITLE]\t[ID]: {data_movie['id_movies'][num]} :[ID]")
            resultat = sorted(resultat, key=lambda x: int(x.split()[0]), reverse=True)
            [print(element) for element in resultat[:top]]
        else:
            print("Ce n'est pas des chiffres !!!")

    def search_years(self, year, sup=None, inf=None):
        resultat = []
        data_movie = self.load_json(path_movie, "r")
        if isinstance(year, int):
            for num, line in enumerate(data_movie['release_movies']):
                if year == line and not sup and not inf:
                    resultat.append(f"{line}\t[TITLE]: {data_movie['title_movies'][num]} :[TITLE]\t[ID]: {data_movie['id_movies'][num]} :[ID]")
                elif year <= line and sup:
                    resultat.append(f"{line}\t[TITLE]: {data_movie['title_movies'][num]} :[TITLE]\t[ID]: {data_movie['id_movies'][num]} :[ID]")
                elif year >= line and inf:
                    resultat.append(f"{line}\t[TITLE]: {data_movie['title_movies'][num]} :[TITLE]\t[ID]: {data_movie['id_movies'][num]} :[ID]")

            if resultat:
                print('-' * 50)
                print(f"Nombre de films trouvés : {len(resultat)}\n")
                resultat = sorted(resultat, key=lambda x: int(x.split()[0]))
                [print(element) for element in resultat]
            else:
                print("Aucun film correspondant")
        else:
            print("Ce n'est pas du texte")

    def search_director(self, director, types="Film Série"):
        resultat = []
        data_movie = self.load_json(path_movie, "r")
        if isinstance(director, str):
            for num, line in enumerate(data_movie['director_movies']):
                try:
                    if director.lower() in line.lower() and data_movie['type_movie'][num] in types:
                        resultat.append(f"{line}\t[TITLE]: {data_movie['title_movies'][num]} :[TITLE]\t[ID]: {data_movie['id_movies'][num]} :[ID]")
                except AttributeError:
                    continue
            if resultat:
                print('-' * 50)
                print(f"Nombre de films trouvés : {len(resultat)}\n")
                [print(element) for element in resultat]
            else:
                print("Aucun film correspondant")
        else:
            print("Ce n'est pas du texte !!!")

    def view(self):
        views = []
        data_movie = self.load_json(path_movie, "r")
        if ids_movie:
            for element in ids_movie:
                index = data_movie['id_movies'].index(element)
                views.append(f"{element}: {data_movie['title_movies'][index]}")
            print('-' * 50)
            [print(element) for element in views]
        else:
            print(f"Nombre de film dans la liste: {len(ids_movie)}. Utiliser la fonction add pour ajouter des films !")

    def add(self, *ids_only):
        for id_only in ids_only:
            if isinstance(id_only, int):
                ids_movie.append(id_only)
            else:
                print("ID ONLY")
        ids_movie.sort()

    def delete(self, *ids_only):
        for id_only in ids_only:
            if isinstance(id_only, int):
                ids_movie.remove(id_only)
            else:
                print("ID ONLY")
        ids_movie.sort()

    # def run(self):
    #     pass
