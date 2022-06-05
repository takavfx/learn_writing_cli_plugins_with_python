import click
from pathlib import Path


@click.command()
@click.argument('path', default=".")
def package(path):
    path = Path(path)
    print("PACKAGING: {}".format(path.absolute()))


@click.command()
@click.option("-i", "--input", required=True)
@click.option("-o", "--output", required=True)
def convert(input, output):
    input_file_path = Path(input)
    output_file_path = Path(output)
    print("CONVERT: {} TO {}".format(input_file_path.absolute(), output_file_path.absolute()))
