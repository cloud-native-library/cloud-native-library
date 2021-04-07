import logging
import mysql.connector
import azure.functions as func
import os
from jinja2 import Template


def jinja2_nico():
            # Connect to MySQL
    cnx = mysql.connector.connect(
        user=os.environ['user'],
        password=os.environ['password'],
        host=os.environ['host'],
        port=3306,
        ssl_ca=os.environ['ssl_ca'],
        database=os.environ['database'])
    logging.info(cnx)

    cursor = cnx.cursor()
    cursor.execute("""SELECT Titre from livres""")
    result = []
    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result.append(row)

    with open('hello.html') as f :
        template=Template(f.read())
    livres = template.render(result=result)
    return livres


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(jinja2_nico(),status_code=200,mimetype="text/html")
