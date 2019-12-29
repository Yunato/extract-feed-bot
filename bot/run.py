import sys
from slackbot.bot import Bot
from bot.controller import Controller
from plugins.my_mention import *


def main():
    args = sys.argv
    if args[1] == "bot":
        bot = Bot()
        bot.run()
    elif args[1] == "fetch":
        fetch()
    elif args[1] == "send":
        send()


if __name__ == "__main__":
    main()
