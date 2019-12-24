import urllib.request
import os
from slackbot.bot import listen_to
from bot.controller import Controller

controller = Controller()

@listen_to('fetch')
def fetch(message):
    controller.add_url("Alice", "https://gigazine.net/index.php?/news/rss_2.0/")
    message.send('get {} feeds'.format(controller.fetch_feed()))

@listen_to('send')
def send(message):
    req = urllib.request.Request(os.environ.get('WEBHOOK_URL'), controller.create_message())
    urllib.request.urlopen(req)
