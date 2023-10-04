import click
import os
from atproto import Client
from mastodon import Mastodon


def bluesky_send(text):
    """Send a text message to BlueSky"""
    user = os.getenv('BLUESKY_USER')
    password = os.getenv('BLUESKY_PASSWORD')

    if user is None:
        print('No BlueSky environment variables found')
        return
    
    client = Client()
    client.login(user, password)

    print(f'Sending "{text}" to BlueSky...')
    client.send_post(text)

def mastodon_send(text):
    """Send a text message to Mastodon"""
    baseurl = os.getenv('MASTODON_URL')
    token = os.getenv('MASTODON_ACCESSTOKEN')
    
    if baseurl is None:
        print('No Mastodon environment variables found')
        return
    
    mastodon = Mastodon(access_token=token, api_base_url=baseurl)
    print(f'Sending "{text}" to Mastodon...')
    mastodon.toot(text)


@click.command('send', short_help='Send message to all services')
@click.argument('text')
def sender(text):
    """Wrapper to send to all services"""
    bluesky_send(text)
    mastodon_send(text)
