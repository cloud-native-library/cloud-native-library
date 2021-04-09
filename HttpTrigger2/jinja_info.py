from jinja2 import Template
from .info_book import info_book


def jinja_info(title):
    # title = title
    result= info_book(title)
    with open('trigger2.html') as f :
        template=Template(f.read())
    livres = template.render(result=result, title=title)
    return livres