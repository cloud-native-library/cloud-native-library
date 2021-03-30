import logging
from .bdd import insert_bdd
import azure.functions as func


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    titre = myblob.name.split("/")[-1]
    insert_bdd(titre, myblob)
