import configparser
import os.path
# from tempfile import TemporaryDirectory
from azure.storage.blob import BlobServiceClient


def download(filename):
    config = configparser.ConfigParser()
    config.read("config.ini")
    blobclient = BlobServiceClient(f"https://{config['storage']['account']}.blob.core.windows.net", config["storage"]["key"])
    containerclient = blobclient.get_container_client(config["storage"]["container"])
    blobclient = containerclient.get_blob_client(os.path.basename(filename))
    dl_folder = config["general"]["restoredir"]
    with open(os.path.join(dl_folder, filename), "wb") as my_blob:
        blob_data = blobclient.download_blob()
        blob_data.readinto(my_blob)


download("Germaine.txt")
