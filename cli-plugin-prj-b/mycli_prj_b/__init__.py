import click


@click.group()
def create():
    pass


@create.command()
@click.option("-n", "--name", default="myapp")
def app(name):
    print("CREATE APP: {}".format(name))


@create.command()
@click.option("-n", "--name", default="myapp")
def task(name):
    print("CREATE TASK: {}".format(name))
