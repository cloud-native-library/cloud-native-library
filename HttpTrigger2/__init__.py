import logging
import azure.functions as func
import mysql.connector
import os


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
    cursor.execute("""SELECT ID,Titre,URL_BLOB from livres""")
    result_list = cursor.fetchall()
    # Build result response text
    result_str_list = []
    for row in result_list:
        row_str = ', '.join([str(v) for v in row])
        result_str_list.append(row_str)
    result_str = '\n'.join(result_str_list)
    return func.HttpResponse(
        result_str,
        status_code=200
    )
