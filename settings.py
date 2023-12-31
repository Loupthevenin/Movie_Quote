import os


# FILTRE pour le scrap
FILTRE = (r"\d+\s*\(\d+\s*votes?\)|\d+.|TagsTopsLiensPartenariatDernièresSagasPersonnagesÀ "
          r"proposMosaïqueProposerMentions légales|TagsTopsLiensPartenariatDernièresSagasPersoÀ "
          r"proposMosaïqueProposerMentions légales"
          r"|Saga|Traduction")
FILTRE_syntax = ["Dr.", "C.I.A", "J.", "2."]


# Data json
path_movie = os.path.join(os.path.dirname(__file__), 'data/data_movies.json')
path_quote = os.path.join(os.path.dirname(__file__), 'data/data_quote.json')
base_data = {"ids": [],
             "quotes": [],
             "character": []
             }


# Setting
url_movie = "https://www.kaakook.fr/film-"  # 20 citations par page

# Valeur par defaut
ids_movie = [13, 14, 15, 29, 37, 67, 68, 228, 282, 452, 477, 577, 588, 597, 862, 891, 993, 997, 1183, 1270, 1325, 1486, 1691, 1868, 1935, 2029, 2030, 2031, 2032, 2088, 2143, 2225, 2505, 2617, 2995, 3248]
quote_list = []  # liste de toutes les citations
character_list = []  # liste de tous les personnages de chaque citation
ids_list = []   # liste de tous les ids de chaque citation
remove_ids_list = []    # liste pour supprimer des films dans la base de donnée
