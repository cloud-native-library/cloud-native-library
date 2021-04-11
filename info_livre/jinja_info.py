import logging
from jinja2 import Template
from .info_book import info_book


def jinja_info(title):
    """
    Template Jinja qui récupère les informations de info_book
    """
    logging.info("début jinja_info")

    result1, result = info_book(title)
    logging.info("import de la fonction info_book")

    with open('info_livre.html') as f:
        template = Template(f.read())
    livres = template.render(result1=result1, result=result, title=title)
    logging.info("Retourne le résultat dans la page html")

    return livres
