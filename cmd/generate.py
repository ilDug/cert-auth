import typer
from core.settings import KEYS_PATH
from core.openssl_commands import PRIV_KEY_GEN

generate_cmd = typer.Typer()


@generate_cmd.command("privkey")
def generate_private_key(
    subject: str = typer.Argument(
        ..., help="il nome del soggetto corrispondente alla chiave privata"
    )
):
    """genera una chiave privata e la salva nell PKI"""
    print(subject)



@generate_cmd.command("request")
def generate_csr():
    pass


@generate_cmd.command("certificate")
def generate_crt():
    pass


@generate_cmd.command("pubkey")
def generate_pubkey():
    pass
