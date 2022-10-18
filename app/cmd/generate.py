from typing import List
import typer
from engine.generator import Generator
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
    g = Generator()
    g.priv_key(subject)


@generate_cmd.command("request")
def generate_csr(
    subject: str = typer.Argument(
        ...,
        help="il nome del soggetto a cui fa riferiment oal chiave privata precedentemente generata",
    ),
    alt_names: List[str] = typer.Argument(
        None, help="lista di COMMON NAME alternativi separata da spazio"
    ),
):
    g = Generator()
    g.request(subject, alt_names)


@generate_cmd.command("certificate")
def generate_crt(
    subject: str = typer.Argument(
        ...,
        help="il nome del soggetto a cui fa riferiment oal chiave privata precedentemente generata",
    ),
    alt_names: List[str] = typer.Argument(
        None, help="lista di COMMON NAME alternativi separata da spazio"
    ),
):
    g = Generator()
    g.priv_key(subject)
    g.request(subject, alt_names)
    g.certificate(subject, alt_names)
