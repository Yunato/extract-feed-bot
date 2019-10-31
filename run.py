import feedparser
from slackbot.bot import Bot

def getFeeds(rss_url):
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
