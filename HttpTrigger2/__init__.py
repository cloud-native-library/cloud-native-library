import logging
import azure.functions as func
from .jinja_info import jinja_info

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

        return func.HttpResponse(jinja_info(title), status_code=200,mimetype="text/html")
    else:
        return func.HttpResponse(
            "Please pass a 'titre' on the query string or in the request body",
            status_code=400)
