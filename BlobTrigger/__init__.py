import logging
from .bdd import insert_bdd
import azure.functions as func


def main(myblob: func.InputStream):
    """
    Est déclenchée lorsqu'un fichier est uploader dans le conteneur.
    Permet de remplir une base de donnée grâce à la fonction insert_bdd
    --------------------------------------------------------------------------
    insert_bdd(titre, myblob)
            titre = titre du livre uploadé
            myblob = objet blob (type : bytes)
    """
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    # Garde juste le nom du fichier
    titre = myblob.name.split("/")[-1].split(".")[0]
    logging.info(f"nom du fichier : {titre}")

    # Appel de la fonction insert_bdd
    logging.info("Appel de la fonction insert_bdd")
    insert_bdd(titre, myblob)
    logging.info("BlobTrigger finished")
