import feedparser
from slackbot.bot import Bot

def getFeed(rss_url):
    for entry in feedparser.parse(rss_url).entries:
        print(entry.title)
        print(entry.link)
        print(entry.category)
        print('----')
    

def main():
    # bot = Bot()
    # bot.run()
    getFeed(RSS_URL)

if __name__ == "__main__":
    main()
