import requests
import time
from datetime import datetime
import json

# Test Change!

auth = "MTA3MTIyMzEzNDE0Mjg2MTM2Mw.Gh8wlN.fLqUqIttRlkAqtKSoG8Ks67PtQJ10gUTtF_JEA"
auth_header = {
        'Authorization': auth
    }
url_prefix = 'https://discord.com/api/v9/'
output_channel = 1071224128562016287

class Bot():
    """A class for storing an self-bot user."""
    def __init__(self, auth) -> None:
        self.auth = auth


def display_typing(channel):
    """Makes the \"Name is typing\" notifier appear in a given channel"""
    requests.post(f"{url_prefix}channels/{channel}/typing")

def send_message(message, channel = ''):
    """Sends a message to a given channel. Outputs to fallback if no channel given."""

    if not channel:
        channel = output_channel

    if isinstance(message, list):
        for each in message:
            send_message(each, channel)
        return

    url = f"{url_prefix}channels/{channel}/messages"

    payload = {
        'content': message
    }
    
    # print('typing for ' + str(60 * (len(message)/800)))

    display_typing(channel=channel)
    time.sleep(min(60 * (len(message)/800), 8))

    res = requests.post(url, payload, headers=auth_header)

    if str(res) == "<Response [401]>":
        print(f"WARNING! AUTH ERROR DURING MESSAGE SEND. {res}")

def get_timestamp(in_time):
    """Returns a discord-formatted timestamp of the current time."""
    current_time = time.time()
    current_time += in_time  * 60
    return f"<t:{int(current_time)}:R>"

def get_channels(guild_id):
    """Returns a list of all channels in a given guild."""
    return json.loads(requests.get(f"{url_prefix}guilds/{guild_id}/channels", {}, headers=auth_header).text)

def get_guilds():
    """Gets all guilds which the bot is in."""
    return json.loads(requests.get(f"{url_prefix}users/@me/guilds", {}, headers=auth_header).text)

def retrieve_messages(channel, limit = 1):
    """Retrieves all messages in a channel up to the limit."""
    return json.loads(requests.get(f"{url_prefix}channels/{channel}/messages", headers=auth_header, params={'limit': limit}).text)


if __name__ == '__main__':
    print("Bot Started.")
    # send_message(f"```START - {datetime.fromtimestamp(time.time()).strftime('%m-%d-%Y, %H:%M')}```", 1071224128562016287)
    # send_message(["Woooooo", "Test"])
    # retrieve_messages(limit=5)
    get_channels(1190425798046384159)


