import logging
import azure.functions as func
import pathlib
import mysql.connector



def get_ssl_cert():
    current_path = pathlib.Path(__file__).parent.parent
    return str(current_path / 'BaltimoreCyberTrustRoot.crt.pem')
    
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Connect to MySQL
    cnx = mysql.connector.connect(
        user="adminaskd@groupeaskd", 
        password='Simplongroupeaskd4', 
        host="groupeaskd.mysql.database.azure.com", 
        port=3306,
        ssl_ca=get_ssl_cert(),
        database="table_askd"
    )
    logging.info(cnx)
    # Show databases
    cursor = cnx.cursor()
    cursor.execute("""SELECT ID,Titre,Infos,URL_BLOB from table_askd""")
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







# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Ajoutez à l'url : ?name=VotreNom",
#              status_code=200
#         )
