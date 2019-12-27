import os
import urllib.request
import sys
from slackbot.bot import Bot
from bot.controller import Controller

def main():         
    args = sys.argv
    if args[1] == "bot":
        bot = Bot()
        bot.run()
    elif args[1] == "fetch":
        fetch()
    elif args[1] == "send":
        send()

def fetch():
    Controller().fetch_feed()

def send():
    controller = Controller()
    req = urllib.request.Request(os.environ.get('WEBHOOK_URL'), controller.create_message())
    urllib.request.urlopen(req)

if __name__ == "__main__":
    main()
