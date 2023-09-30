import os


# FILTRE pour le scrap
FILTRE = (r"\d+\s*\(\d+\s*votes?\)|\d+.|TagsTopsLiensPartenariatDernièresSagasPersonnagesÀ "
          r"proposMosaïqueProposerMentions légales|TagsTopsLiensPartenariatDernièresSagasPersoÀ "
          r"proposMosaïqueProposerMentions légales"
          r"|Saga|Traduction")
FILTRE_syntax = ["Dr."]


# Data json
path = os.path.join(os.path.dirname(__file__), 'data/data_quote.json')
base_data = {"ids": [],
             "quotes": [],
             "character": []
             }


# Setting
url_movie = "https://www.kaakook.fr/film-"  # 20 citations par page

ids_movie = [29, 67, 68, 993, 997, 1691]  # matrix, matrix 2, matrix 3, inception, Donnie Darko, HP 1,
quote_list = []  # liste de toutes les citations
character_list = []  # liste de tous les personnages de chaque citation
ids_list = []   # liste de tous les ids de chaque citation
