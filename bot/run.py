import sys
from slackbot.bot import Bot
from bot.controller import Controller
import plugins.my_mention

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
