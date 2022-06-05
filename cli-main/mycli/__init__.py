import click


@click.group()
def main():
    pass


@main.command()
@click.option('-n', '--name', required=True, type=str)
def create(name):
    print("START CREATE: {}".format(name))


@main.command()
def plugins():
    from importlib import metadata
    eps = metadata.entry_points()
    if eps.get("mycli"):
        mycli_eps = eps["mycli"]
        for ep in mycli_eps:
            print(ep)


def cli():
    from importlib import metadata
    eps = metadata.entry_points()
    if eps.get("mycli"):
        mycli_eps = eps["mycli"]
        for ep in mycli_eps:
            plugin = ep.load()
            main.add_command(plugin)
    main()
