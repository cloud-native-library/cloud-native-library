import mysql.connector
import os
import logging
from mysql.connector import errorcode
from .listage_livre import listage_livre


# Obtain connection string information from the portal
config = {
    'host': os.environ['host'],
    'user': os.environ['user'],
    'password': os.environ['password'],
    'database': os.environ['database'],
    'client_flags': [mysql.connector.ClientFlag.SSL],
    'ssl_ca': os.environ['ssl_ca']
}


def connection():
    """
    Permet de se connecter à la base de donnée via les informations
    présent dans la partie config
    """
    # Construct connection string
    try:
        conn = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logging.error("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logging.error("Database does not exist")
        else:
            logging.error(err)
    else:
        cursor = conn.cursor()
        return conn, cursor


def insert_bdd(title, myblob):
    """
    Insert dans la base de donnée les informations voulues :
        id : Valeur auto-incrémenter (Primary Key)
        Titre : titre du livre (Primary Key)
        Infos : Dictionnaire de tous les mots
                avec le nombre d'apparition
        Total : Nombre de mots dans le fichier
        URL_BLOB = url du blob
    """
    logging.info("Début de la connexion à la database")
    conn, cursor = connection()
    logging.info("Connection established")
    # Drop previous table of same name if one exists
    # cursor.execute("DROP TABLE IF EXISTS table_askd;")
    # logging.info("Finished dropping table (if existed).")

    # Create table
    logging.info("Début de la création de la table")
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS table_askd (
            ID serial PRIMARY KEY,
            Titre VARCHAR(255) PRIMARY KEY,
            Infos VARCHAR(255),
            Total INTEGER,
            URL_BLOB VARCHAR(255));""")
    logging.info("Finished creating table.")

    # Récupération des infos dans la fonction listage_livre
    logging.info(f"Récupération des infos sur le livre {title}")
    Infos, Total = listage_livre(myblob)
    logging.info(f"Fin de la récupération des infos sur le livre {title}")

    # Insert some data into table
    url = "https://stockageaskd.blob.core.windows.net/storageblobaskd/"
    logging.info("Début insertion du livre dans la base")
    cursor.execute("""INSERT INTO table_askd (
        Titre, Infos, Total, URL_BLOB)
        VALUES (%s, %s, %s, %s);""", (title, Infos, Total, url+title))
    logging.info("Inserted", cursor.rowcount, "row(s) of data.")

    # Cleanup
    conn.commit()
    logging.info("Commit")
    cursor.close()
    conn.close()
    logging.info(f"Close {cursor} and {conn}")
    logging.info("Done.")
