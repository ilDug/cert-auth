from pathlib import Path
import typer
from engine.importer import Importer
from core.settings import PKI_PATH
from engine.installer import Installer


def install_fn():
    """genera tutta l'infrastruttira della PKI compreso il certificato root"""

    typer.echo("installazione della PRIVATE KEY INFRASCTRUCTURE")
    installer = Installer()

    # controlla che la directory esista
    if PKI_PATH.exists():
        _continue = typer.confirm(
            "l'infrastruttura è già stata inizializzata. Se si prosegue tutti i dati verranno cancellati. Continuare? ",
            abort=True,
        )

        if _continue:
            typer.echo("cancella tutto quello che c'è nella directory PKI")
            installer.clean_structure()

    typer.echo(
        "crea una struttura di file e cartelle iniziale usando le impostazioni classiche"
    )
    installer.scaffolding()

    typer.echo("genera una passprhase per la CA")
    installer.generate_passphrase()

    typer.echo("genera la chiave privata CA")
    installer.create_ca_key()

    typer.echo("genera il certificato CA")
    installer.create_ca_crt()

    typer.echo("verifica il certificato")
    installer.verify_ca_crt()

    typer.echo("ottinene e salva lachiave pubblica CA")
    installer.generate_public_key()


def install_with_existing_root():
    """genera tutta l'infrastruttira della PKI importando la chiave ed il certificato root"""
    raise Exception("metodo non ancora implementato")
    importer = Importer()
    importer.import_ca()
    importer.verify_ca_crt()
    importer.generate_public_key()
