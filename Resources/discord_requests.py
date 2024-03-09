import requests
import time
from datetime import datetime

auth = "MTA3MTIyMzEzNDE0Mjg2MTM2Mw.G_UAaE.0e-LxP0wId0OEKfAkbf35t5ub3GToO37Dsq6vk"
auth_header = {
        'Authorization': auth
    }
url_prefix = 'https://discord.com/api/v9/'
output_channel = 1071224128562016287

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
    
    print('typing for ' + str(60 * (len(message)/800)))
    display_typing(channel=channel)
    time.sleep(min(60 * (len(message)/800), 8))
    res = requests.post(url, payload, headers=auth_header)

if __name__ == '__main__':
    print("Bot Started.")
    send_message(f"```START - {datetime.fromtimestamp(time.time()).strftime('%m-%d-%Y, %H:%M')}```", 1071224128562016287)
    send_message(["Woooooo", "Test"])


