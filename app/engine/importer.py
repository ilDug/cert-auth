import os
from pathlib import Path
import subprocess

from .installer import Installer
import typer
from core.settings import CA_KEY_PATH, PASSPRHASE_PATH, CA_CRT_PATH


class Importer(Installer):
    def import_ca(self):
        cert_path = typer.prompt("inserire il contenuto del certificato CA")
        CA_CRT_PATH.write_text(cert_path)

        key_path = typer.prompt("inserire il contenuto  della chiave privata CA .key")
        CA_CRT_PATH.write_text(key_path)

        passphrase = typer.prompt("inserire la passphrase")
        PASSPRHASE_PATH.write_text(passphrase)
        PASSPRHASE_PATH.chmod(400)

        cmd = f"openssl rsa -check -in {CA_KEY_PATH}  -noout -text -passin file:{PASSPRHASE_PATH}"
        res = subprocess.run([cmd], stdout=subprocess.PIPE).stdout.decode("utf-8")
        print(res)
        # os.system(cmd)
