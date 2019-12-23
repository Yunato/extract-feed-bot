import feedparser
import pytz
from datetime import datetime
from slackbot.bot import Bot
from bot.feed import Feed

RSS_URL = "example.com"

def get_feeds(rss_url):
    if not rss_url:
        raise ValueError("The argument must be not empty")

    LOCAL_TZ = pytz.timezone("Asia/Tokyo")
    UTC = pytz.timezone("UTC")

    d = feedparser.parse(rss_url)
    source = d['feed']['title']

    for entry in range(len(d.entries)):
        title = d.entries[entry].title
        link = d.entries[entry].link
        time = datetime(*d.entries[entry].updated_parsed[:6], tzinfo=UTC).astimezone(LOCAL_TZ)
        summary = d.entries[entry].summary
        category = d.entries[entry].category
        print(Feed(title, link, source, time, summary, category))
        print('----')
    return d.entries
                    
                    
def main():         
    # bot = Bot()
    # bot.run()
    get_feeds(RSS_URL)

if __name__ == "__main__":
    main()
