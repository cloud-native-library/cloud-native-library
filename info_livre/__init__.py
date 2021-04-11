import azure.functions as func
import logging
from .jinja_info import jinja_info


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Si le paramètre 'title' est présent dans l'url, renvoie la fonction
    jinja_info(title)
    Si le paramètre 'title' est absent dans l'url, demande d'entrée un titre
    dans l'url
    """
    logging.info('Python HTTP trigger function processed a request.')
    title = req.params.get('title')
    logging.info(f"Titre = {title}")

    if title:
        logging.info("Titre présent")
        return func.HttpResponse(
            jinja_info(title),
            status_code=200,
            mimetype="text/html"
            )

    if not title:
        logging.info("Titre absent")
        return func.HttpResponse(
            "Please pass a 'titre' on the query string or in the request body",
            status_code=400
            )
