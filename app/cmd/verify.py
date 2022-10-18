from typing import List
import typer
from engine.certificate import Certificate

verify_cmd = typer.Typer()


@verify_cmd.command("cert")
def verify_certificate(subject: str = typer.Argument(..., help="il nome del soggetto")):
    c = Certificate()
    c.verify(subject)
