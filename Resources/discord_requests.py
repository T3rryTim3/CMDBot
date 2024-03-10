import requests
import time
from datetime import datetime
import json

url_prefix = 'https://discord.com/api/v10/'

class bcolors:
    """A class containing constants for text colors"""
    reset = '\033[0m'
    bold = '\033[01m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

class Bot():
    """A class for storing an self-bot user.
    -
    Parameters:
    auth: The token of the user
    default_output: The default channel which the bot will output to."""

    def __init__(self, auth, default_output) -> None:
        self.auth = auth
        self.auth_header = {
            "Authorization": self.auth,
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
            "Accept": '*/*'
        }
        self.default_output = default_output

        self.user_info = json.loads(requests.get(f"{url_prefix}users/@me", {}, headers=self.auth_header).text)

        self.username = self.user_info["username"]
        self.id = self.user_info['id']
        self.global_name = self.user_info["global_name"]

        print(f"{bcolors.green}{self.username} Bot started.{bcolors.reset}")

    def __str__(self):
        return self.username

    def get_channels(self, guild_id):
        """Returns a list of all channels in a given guild."""
        return json.loads(requests.get(f"{url_prefix}guilds/{guild_id}/channels", {}, headers=self.auth_header).text)

    def get_guilds(self):
        """Gets all guilds which the bot is in."""
        return json.loads(requests.get(f"{url_prefix}users/@me/guilds", {}, headers=self.auth_header).text)

    def retrieve_messages(self, channel, limit = 1):
        """Retrieves all messages in a channel up to the limit."""
        return json.loads(requests.get(f"{url_prefix}channels/{channel}/messages", headers=self.auth_header, params={'limit': limit}).text)

    def display_typing(self, channel):
        """Makes the \"Name is typing\" notifier appear in a given channel"""
        requests.post(f"{url_prefix}channels/{channel}/typing")

    def send_message(self, message, channel = ''):
        """Sends a message to a given channel. Outputs to fallback if no channel given."""

        if not channel:
            channel = self.default_output

        if isinstance(message, list):
            for each in message:
                self.send_message(each, channel)
            return

        url = f"{url_prefix}channels/{channel}/messages"

        payload = {
            'content': message
        }
        
        # print('typing for ' + str(60 * (len(message)/800)))

        self.display_typing(channel=channel)
        time.sleep(min(60 * (len(message)/800), 8))

        res = requests.post(url, payload, headers=self.auth_header)

        if str(res) == "<Response [401]>":
            print(f"WARNING! AUTH ERROR DURING MESSAGE SEND. {res}")    

def get_timestamp(in_time):
    """Returns a discord-formatted timestamp of the current time + in_time (in seconds)"""
    current_time = time.time()
    current_time += in_time * 60
    return f"<t:{int(current_time)}:R>"

if __name__ == '__main__':
    bot = Bot("MTIxNjE1ODg4NDk4MTUwNjE0OA.GXmUbv.3L_py82sE8Uylrum17HkuACGK6YefFBXHRqi_Y", 1216166579843235863)
    print(bot.retrieve_messages(1216166579843235863, 1))