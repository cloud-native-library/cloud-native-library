import logging
import azure.functions as func
import mysql.connector
import os
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Connect to MySQL
    cnx = mysql.connector.connect(
        user=os.environ['user'],
        password=os.environ['password'],
        host=os.environ['host'],
        port=3306,
        ssl_ca=os.environ['ssl_ca'],
        database=os.environ['database']
    )

    logging.info(cnx)

    # Show databases
    cursor = cnx.cursor()
    cursor.execute("""SELECT Titre from livres""")
    result = []
    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result.append(row)
        
    return func.HttpResponse("\n".join(result), status_code=200,mimetype="text/html")
