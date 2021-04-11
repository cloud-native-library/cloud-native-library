import logging
from jinja2 import Template
from .list_books import list_books


def jinja_books():
    """
    Template Jinja qui récupère les informations de list_books
    """
    logging.info("début jinja_books")

    result = list_books()
    logging.info("import de la fonction list_books")

    with open('liste_livres.html') as f:
        template = Template(f.read())
    livres = template.render(result=result)
    logging.info("Retourne le résultat dans la page html")

    return livres
