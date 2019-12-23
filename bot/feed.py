import feedparser
import pytz
from datetime import datetime

class Feed:

    def __init__(self, title, link, source, time, summary):	
        self.title = title
        self.link = link
        self.source = source
        self.time = time.strftime("%Y/%m/%d %H:%M:%S") 
        self.summary = summary
        # self.category = category

    def __repr__(self):
        return "title: %s\nlink: %s\nsource: %s\ntime: %s\nsummary: %s" % (self.title, self.link, self.source, self.time, self.summary)
        # return "title: %s\nlink: %s\nsource: %s\ntime: %s\nsummary: %s\ncategory: %s" % (self.title, self.link, self.source, self.time, self.summary, self.category)

    @staticmethod
    def fetch_feed(rss_url):
        if not rss_url:
            raise ValueError("The argument must be not empty")

        LOCAL_TZ = pytz.timezone("Asia/Tokyo")
        UTC = pytz.timezone("UTC")

        d = feedparser.parse(rss_url)
        source = d['feed']['title']

        feeds = []
        for entry in range(len(d.entries)):
            title = d.entries[entry].title
            link = d.entries[entry].link
            time = datetime(*d.entries[entry].updated_parsed[:6], tzinfo=UTC).astimezone(LOCAL_TZ)
            summary = d.entries[entry].summary
            feeds.append(Feed(title, link, source, time, summary))
        return feeds
