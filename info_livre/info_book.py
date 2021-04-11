import logging
import mysql.connector
import os


logging.info("Début connexion")
cnx = mysql.connector.connect(
        user=os.environ['user'],
        password=os.environ['password'],
        host=os.environ['host'],
        port=3306,
        ssl_ca=os.environ['ssl_ca'],
        database=os.environ['database'])
cursor = cnx.cursor()
logging.info(cursor)


def info_book(title):
    """
    Sélectionne les mots + totals en fonction du titre sélectionné
    """
    logging.info("Début info_book")

    result = []
    result1 = []
    cursor.execute("""SELECT
        Titre, Total, URL_BLOB
        from livres
        WHERE Titre = %s;""", (title,))
    logging.info("Sélection des colonnes Titre, Total et URL_BLOB")

    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result1.append(row)
    logging.info("Ajout du livre sélectionné dans une liste")

    cursor.execute("SELECT Words, Total from mots WHERE Titre = %s;", (title,))
    logging.info(f"Sélection des mots appartenant au livre {title}")

    result = []
    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result.append(row)
    logging.info("Ajout des mots dans une liste")

    logging.info("Retourne la liste des mots + total")
    return result1, result
