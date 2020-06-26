import click


@click.command()
@click.argument('mark', type=click.STRING)
def run(mark):
    click.echo(mark)
