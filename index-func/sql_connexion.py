import mysql.connector
import os
import logging


cnx = mysql.connector.connect(
        user=os.environ['user'],
        password=os.environ['password'],
        host=os.environ['host'],
        port=3306,
        ssl_ca=os.environ['ssl_ca'],
        database=os.environ['database'])
logging.info(cnx)
cursor = cnx.cursor()

def list_books():
    cursor.execute("""SELECT Titre from livres""")
    result = []
    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result.append(row)
    return result