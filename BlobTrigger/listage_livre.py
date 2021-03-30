import re
import json
import unicodedata
import codecs


def listage_livre(myblob):
    res = {}
    liste = []
    file = myblob.read()
    file = codecs.decode(file, 'latin-1')
    file = re.split(r'\W', file)
    total = len(file)
    for char in file:
        char = char.lower()
        char = ''.join(
            (c for c in unicodedata.normalize('NFD', char)
                if unicodedata.category(c) != 'Mn')
                )
        liste.append(char)
    for char in liste:
        res[char] = liste.count(char)
    print(res)
    print("Nombre de mot :", total)
    return json.dumps(res), total
