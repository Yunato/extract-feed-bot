import concurrent.futures
import time
import datetime
from slackbot.bot import Bot
from plugins.my_mention import *


def run():
    bot = Bot()
    bot.run()


def fetcher():
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    now = datetime.datetime.now(JST)
    std = datetime.datetime(now.year, now.month, now.day, (int(now.hour/2) + 1) * 2, 0, 0, tzinfo=JST)
    td = datetime.timedelta(hours=2)
    while True:
        dt_now = datetime.datetime.now(JST)
        if std < dt_now:
            std = dt_now + td
            fetch()


def sender():
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    now = datetime.datetime.now(JST)
    if now.hour > 20 and now.minute > 0 and now.second > 0:
        day = now.day + 1
    else:
        day = now.day
    std = datetime.datetime(now.year, now.month, day, 20, 0, 0, tzinfo=JST)
    td = datetime.timedelta(days=1)
    while True:
        dt_now = datetime.datetime.now(JST)
        if std < dt_now:
            std = dt_now + td
            send()


def main():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    executor.submit(run)
    executor.submit(fetcher)
    executor.submit(sender)


if __name__ == "__main__":
    main()
