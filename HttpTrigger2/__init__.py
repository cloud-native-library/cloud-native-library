import logging
import azure.functions as func
import mysql.connector
import os
from jinja2 import Template

cnx = mysql.connector.connect(
        user=os.environ['user'],
        password=os.environ['password'],
        host=os.environ['host'],
        port=3306,
        ssl_ca=os.environ['ssl_ca'],
        database=os.environ['database']
    )

cursor = cnx.cursor()


def info_book(title):
    cursor.execute(
    """SELECT Words, Total from mots WHERE Titre = %s;""",
    (title,))
    result=[]
    for row in cursor.fetchall():
        row = ', '.join([str(v) for v in row])
        result.append(row)
    return row



def jinja_info(title):
    title = title
    result= info_book(title)
    with open('trigger2.html') as f :
        template=Template(f.read())
    livres = template.render(result=result, title=title)
    return livres

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
      

        logging.info(cnx)

        # cursor.execute(
        #     "SELECT Titre, Total, URL_BLOB from livres WHERE Titre = %s;",
        #     (title,))
        # for row in cursor.fetchall():
        #     row = ', '.join([str(v) for v in row])
        #     result.append(row)

        # cursor.execute(
        #     "SELECT Words, Total from mots WHERE Titre = %s;",
        #     (title,))
        # for row in cursor.fetchall():
        #     row = ', '.join([str(v) for v in row])
        #     result.append(row)
        # return result   

        


        return func.HttpResponse(jinja_info(title), status_code=200,mimetype="text/html")
    else:
        return func.HttpResponse(
            "Please pass a 'titre' on the query string or in the request body",
            status_code=400)
