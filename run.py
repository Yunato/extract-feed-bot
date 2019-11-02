import feedparser
from dao import Dao
from slackbot.bot import Bot

RSS_URL = "example.com"

def get_feeds(rss_url):
    if not rss_url:
        raise ValueError("The argument is empty")
    entries = feedparser.parse(rss_url).entries
    for entry in entries:
        print(entry.title)
        print(entry.link)
        print(entry.category)
        print('----')
    return entries
    

def main():
    # bot = Bot()
    # bot.run()
    get_feeds(RSS_URL)

if __name__ == "__main__":
    main()
