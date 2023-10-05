# BlueSky-Mastodon

Basic command-line-interface (CLI) scripts to post to BlueSky and Mastodon simultaneously.
Requires the following environment variables:

    BLUESKY_USER          - full user name (without @)
    BLUESKY_PASSWORD      - application password (Settings -> App passwords)
    MASTODON_URL          - base url for instance; eg, https://mastodon.social/
    MASTODON_ACCESSTOKEN  - application access token (Settings -> Development)

## Installation

Clone/download this repo and run: `pip install .` on the main directory. You can then access the CLI from whichever environment you installed it in.

## Usage

```
social --help
Usage: social [OPTIONS] COMMAND [ARGS]...

  Command-line tool for interfacing with BlueSky and Mastodon

Options:
  --help  Show this message and exit.

Commands:
  get   Fetch messages
  send  Send message to all services
```

If you have your environment variables set up, you can send messages with: `social send 'This is a post using python!'`

The `get` API is not yet fully functional.

Only text messages can be sent at this time.
