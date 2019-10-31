import feedparser
from slackbot.bot import Bot

RSS_URL = ""

def getFeeds(rss_url):
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
    getFeeds(RSS_URL)

if __name__ == "__main__":
    main()
