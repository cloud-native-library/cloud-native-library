from jinja2 import Template
from .sql_connexion import list_books


def jinja_books():

    result= list_books()
    with open('livres.html') as f :
        template=Template(f.read())
    livres = template.render(result=result)
    return livres