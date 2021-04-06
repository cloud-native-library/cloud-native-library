import logging
import azure.functions as func
import mysql.connector
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    title = req.params.get('title')

    if not title:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            title = req_body.get('title')

    if title:
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
        result = []

        cursor.execute(
            """SELECT Titre, Total, URL_BLOB from livres WHERE Titre = %s;""",
            (title,))
        for row in cursor.fetchall():
            row = ', '.join([str(v) for v in row])
            result.append(row)

        cursor.execute(
            """SELECT Words, Total from mots WHERE Titre = %s;""",
            (title,))
        for row in cursor.fetchall():
            row = ', '.join([str(v) for v in row])
            result.append(row)

        return func.HttpResponse("\n".join(result), status_code=200)

    else:
        return func.HttpResponse(
            "Please pass a 'titre' on the query string or in the request body",
            status_code=400)
