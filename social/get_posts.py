import os
import click
from atproto import Client

@click.command('get', short_help='Fetch messages')
# @click.argument('handle', default=None)
def bluesky_get(handle: str=None):
    client = Client()
    user = os.getenv('BLUESKY_USER')
    password = os.getenv('BLUESKY_PASSWORD')
    client.login(user, password)

    # Default to the user
    # if handle is None:
    handle = user

    print(f'\nBlueSky Profile Posts of {handle}:\n\n')

    # Get profile's posts. Use pagination (cursor + limit) to fetch all
    profile_feed = client.app.bsky.feed.get_author_feed({'actor': handle})
    for feed_view in profile_feed.feed:
        print('-', feed_view.post.record.text)

