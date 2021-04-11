import azure.functions as func
import logging
from .jinja_liste import jinja_books


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Renvoie les informations de la fonction jinja_books
    """
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
        jinja_books(),
        status_code=200,
        mimetype="text/html"
        )
