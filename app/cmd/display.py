from typing import List
import typer
from engine.certificate import Certificate


display_cmd = typer.Typer()


@display_cmd.command("privkey")
def display_priv_key(
    subject: str = typer.Argument(..., help="il nome del soggetto"),
    pem: bool = typer.Option(
        False, "--pem", "-p", help="mostra l'elemente nella forma codificata"
    ),
):
    c = Certificate()
    c.priv_key(subject, pem)


@display_cmd.command("pubkey")
def display_pub_key(subject: str = typer.Argument(..., help="il nome del soggetto")):
    c = Certificate()
    c.pub_key(subject)


@display_cmd.command("cert")
def display_cert(
    subject: str = typer.Argument(..., help="il nome del soggetto"),
    pem: bool = typer.Option(
        False, "--pem", "-p", help="mostra l'elemente nella forma codificata"
    ),
):
    c = Certificate()
    c.cert(subject, pem)
