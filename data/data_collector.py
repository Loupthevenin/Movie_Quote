from functions import *
from settings import *
import json
import os


data_movies = {"title_movies": [],
               "type_movie": [],
               "id_movies": [],
               "director_movies": [],
               "release_movies": [],
               "number_quotes": []
               }


state_number = 3300
i = 1


if not os.path.exists(path_movie):
    with open(path_movie, 'w') as file_json:
        json.dump({}, file_json)


def update_database(data):
    title_all = soups.find('h1').text
    if "Erreur 410" in title_all:
        print("page non trouvé")
    elif "Erreur 404" in title_all:
        print("page non trouvé")
    else:
        if "Film" in title_all:
            data['title_movies'].append(title_all.replace('Film - ', ""))
            data['type_movie'].append("Film")
        elif "Série" in title_all:
            data['title_movies'].append(title_all.replace('Série - ', ""))
            data['type_movie'].append("Série")
        data['id_movies'].append(i)
        data['director_movies'].append(find_tag_dd(soups, 2))
        data['release_movies'].append(find_tag_dd(soups, 3))
        data['number_quotes'].append(find_tag_dd(soups, 4))


with open(path_movie, 'r', encoding="utf-8") as f:
    db = json.load(f)


if data_movies.keys() == db.keys() and db['id_movies']:
    encode = 1
    i = db['id_movies'][-1] + 1
    while not i > state_number:
        print(i)
        soups = html_soup(url_movie, i, 1)
        if soups != "ERROR":
            update_database(db)
            i += 1
        elif soups == "ERROR":
            i += 1
            continue
else:
    encode = 2
    while not i > state_number:
        print(i)
        soups = html_soup(url_movie, i, 1)
        if soups != "ERROR":
            update_database(data_movies)
            i += 1
        elif soups == "ERROR":
            i += 1
            continue


if encode == 1:
    with open(path_movie, 'w', encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)
elif encode == 2:
    with open(path_movie, 'w', encoding="utf-8") as f:
        json.dump(data_movies, f, ensure_ascii=False, indent=4)
