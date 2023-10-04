import click
from social.send_post import sender
from social.get_posts import bluesky_get


@click.group('pyaci')
def cli():
    """Command-line tool for interfacing with BlueSky and Mastodon"""

cli.add_command(sender)
cli.add_command(bluesky_get)

if __name__ == '__main__':
    cli()
