import os
import click
from atproto import Client
from mastodon import Mastodon


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


def mastodon_get():
    """Get messages from Mastodon"""
    baseurl = os.getenv('MASTODON_URL')
    token = os.getenv('MASTODON_ACCESSTOKEN')

    if baseurl is None:
        print('No Mastodon environment variables found')
        return

    # TODO: Not working yet
    mastodon = Mastodon(access_token=token, api_base_url=baseurl)
    user = mastodon.account_search(None)  # call to search user
    print(user)
    id = user[0]['id']
    print(id)
    feed = mastodon.timeline(f'list/{id}')
    print(feed)


@click.command('get', short_help='Fetch messages')
def getter():
    bluesky_get()
    # mastodon_get()
