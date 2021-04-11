import logging
import re
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
    logging.info(f"Lecture de l'objet {myblob}")

    # Décodage du blob pour permettre son traitement
    file = codecs.decode(file, 'latin-1')
    logging.info("Décodage du blob en latin-1 pour traitement")

    # Split avec regex sur tous les signes de ponctuation
    file = re.split(r'\W', file)
    logging.info("Retrait des signes de ponctuations dans le fichier")

    # Compte le nombre de mot dans le fichier
    total = len(file)
    logging.info("Calcul du nombre de mot dans le fichier")
    logging.info(total)

    # Pour chaque mot dans le fichier
    for char in file:
        char = char.lower()

        # Permet de retirer les accents des mots (merci internet)
        char = ''.join(
            (c for c in unicodedata.normalize('NFD', char)
                if unicodedata.category(c) != 'Mn')
                )
        liste.append(char)
    logging.info("Mise en minuscule de chaque mot")
    logging.info("Retrait des accents dans les mots")

    # Pour chaque mot dans la liste:
    for char in liste:
        # Compte le nombre de fois qu'il apparait pour mettre en format dict
        res[char] = liste.count(char)
    logging.info(res)

    # Return le nombre total de mot + le dictionnaire
    return res, total
