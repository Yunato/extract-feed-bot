import urllib.request
import os
from slackbot.bot import listen_to
from slackbot.bot import respond_to
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

@respond_to('(.*)')
def exec_command_with_one_arg(message, args):
    len_arg = len(args.split())
    if len_arg > 0:
        command = args.split()[0]
        if len(args.split()) == 2:
            arg = args.split()[1]
            message.send('{}'.format(arg))
            return
        elif len(args.split()) == 3:
            arg1 = args.split()[1]
            arg2 = args.split()[2]
            message.send('{} {}'.format(arg1, arg2))
            return
    message.send('Invalid command')

