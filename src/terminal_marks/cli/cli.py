import click
import os

from terminal_marks.api import get_input


@click.command()
@click.argument('mark', type=click.STRING)
def run(mark):
    i = get_input()
    i.mark_name = mark
    i.read_cwd()
    print(i.mark_name, i.directory.as_posix())
