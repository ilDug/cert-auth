from distutils.command.install_headers import install_headers
from pathlib import Path
import typer
from core.settings import PKI_PATH
from cmd.install import install_fn, install_with_existing_root
from cmd.generate import generate_cmd
from cmd.display import display_cmd
from cmd.verify import verify_cmd

app = typer.Typer()
app.add_typer(generate_cmd, name="generate", help="genera un elemento (vedi opzioni)")
app.add_typer(
    display_cmd, name="display", help="visualizza gli elementi (vedi opzioni)"
)
app.add_typer(verify_cmd, name="verify", help="verifica il certificato (vedi opzioni)")


@app.command("install")
def install_cmd(
    import_root: bool = typer.Option(
        False,
        "--import",
        "-i",
        help="importa un certificato, la sua chiave privata. Genera tutta l'infrastruttira della PKI importando la chiave ed il certificato root ",
    )
):
    """genera tutta l'infrastruttira della PKI compreso il certificato root"""

    if not import_root:
        install_fn()
    else:
        install_with_existing_root()


@app.command()
def pubkey():
    """restituisce la chiave pubblica"""
    pass


#    TO DO
#         sign:       firma un file
#         verify-sign:     verifica la firma
#         verify-cert:     verifica un certificato
#         crypt:      cripta un file
#         decrypt:    decripta un file


@app.callback()
def main(ctx: typer.Context):
    typer.secho(
        "--- ilDug --- \n\n******************************************\nCERTIFICATE AUTHORITY\n******************************************\n",
        fg=typer.colors.BRIGHT_MAGENTA,
    )

    typer.echo()
    cwd = Path(PKI_PATH)
    is_empty = not any(cwd.iterdir())
    # controlla che sia installato il sistema di CA
    if (not cwd.exists() or is_empty) and ctx.invoked_subcommand != "install":
        exit_msg = typer.style(
            "prima di utilizzare il programma esegui l'inizializzazione con il comando 'install'",
            fg=typer.colors.BRIGHT_RED,
        )

        raise typer.Exit(typer.echo(exit_msg))


if __name__ == "__main__":
    app()
    # typer.run(main)
