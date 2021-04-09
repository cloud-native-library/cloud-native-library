import logging
import azure.functions as func
from .jinja_liste import jinja_books


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(jinja_books(),status_code=200,mimetype="text/html")
