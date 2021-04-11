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


def list_books():
    """
    Sélectionne la liste des livres
    """
    logging.info("Début list_books")

    cursor.execute("""SELECT Titre from livres""")
    logging.info("Sélection de la colonne Titre")

    result = []
    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result.append(row)
    logging.info("Ajout des livres dans une liste")

    logging.info("Retourne la liste des livres")
    return result
