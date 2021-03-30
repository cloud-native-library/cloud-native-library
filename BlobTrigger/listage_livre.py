import re
import json
import unicodedata
import codecs


def listage_livre(myblob):
    """
    Permet de compter le nombre d'apparition de chaque mot
    et de compter le nombre de mot total dans le fichier
    """
    # Création de dictionnaire vite et liste vide
    res = {}
    liste = []

    # Lecture de l'objet myblob
    file = myblob.read()

    # Décodage du blob pour permettre son traitement
    file = codecs.decode(file, 'latin-1')

    # Split avec regex sur tous les signes de ponctuation
    file = re.split(r'\W', file)

    # Compte le nombre de mot dans le fichier
    total = len(file)

    # Pour chaque mot dans le fichier
    for char in file:
        char = char.lower()

        # Permet de retirer les accents des mots
        char = ''.join(
            (c for c in unicodedata.normalize('NFD', char)
                if unicodedata.category(c) != 'Mn')
                )
        liste.append(char)
    for char in liste:
        # Pour chaque mot, compte le nombre de fois qu'il apparait
        res[char] = liste.count(char)

    print(res)
    print("Nombre de mot :", total)
    return json.dumps(res), total
