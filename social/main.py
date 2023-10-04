import click
from social.send_post import sender
from social.get_posts import getter


@click.group('pyaci')
def cli():
    """Command-line tool for interfacing with BlueSky and Mastodon"""

cli.add_command(sender)
cli.add_command(getter)

if __name__ == '__main__':
    cli()
