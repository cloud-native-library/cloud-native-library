import mysql.connector
import logging
import os

# logging.info("Début connexion")
cnx = mysql.connector.connect(
        user=os.environ['user'],
        password=os.environ['password'],
        host=os.environ['host'],
        port=3306,
        ssl_ca=os.environ['ssl_ca'],
        database=os.environ['database']
    )
cursor = cnx.cursor()
# logging.info(cursor)

def info_book(title):
    
    cursor.execute(
    "SELECT Words, Total from mots WHERE Titre = %s;",
    (title,))
    result=[]
    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result.append(row)
    return result