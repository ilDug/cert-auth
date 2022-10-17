from pathlib import Path
import typer
from core.settings import PKI_PATH
from cmd.install import install_cmd
from cmd.generate import generate_cmd

app = typer.Typer()
app.add_typer(generate_cmd, name="generate", help="genera un elemento(vedi opzioni)")
app.add_typer(
    install_cmd,
    name="install"
)


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
    print(cwd)

    # controlla che sia installato il sistema di CA
    if not cwd.exists() and ctx.invoked_subcommand != "install":
        exit_msg = typer.style(
            "prima di utilizzare il programma esegui l'inizializzazione con il comando 'install'",
            fg=typer.colors.BRIGHT_RED,
        )

        raise typer.Exit(typer.echo(exit_msg))


if __name__ == "__main__":
    app()
    # typer.run(main)
