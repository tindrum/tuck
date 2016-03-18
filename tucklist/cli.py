import click, os


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.option('--history', '-h', is_flag=True, help='Get last command from bash history.')
@click.argument('name', default='world', required=False)
def main(name, as_cowboy, history):
    """Save and search snippets to TuckEverListing website."""
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))
    if history:
        # localHistory = os.system("history 2")
        # hist = ""
        # os.system('history 4')
        # click.echo('History is {0}'.format(os.system('history 4')))
        click.echo('listing is  {0}'.format(os.system('ls')))
        # TODO: it shows the listing from current directory, but will it always? 
        #       I guess since I'm really interested in the history, I don't care much
        #       which path is actually being used. Unless it matters for 'history' too.
        # TODO: 'ls' will send its output to python, but 'history <n>' will not. Why not?
