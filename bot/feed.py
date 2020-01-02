import feedparser
import pytz
import re
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
        d = feedparser.parse(rss_url)
        source = d['feed']['title']
        LOCAL_TZ = pytz.timezone("Asia/Tokyo")
        UTC = pytz.timezone("UTC")
        p = re.compile(r"<[^>]*?>")

        feeds = []
        for index in range(len(d.entries)):
            title = d.entries[index].title
            link = d.entries[index].link
            time = datetime(*d.entries[index].updated_parsed[:6], tzinfo=UTC).astimezone(LOCAL_TZ)
            summary = p.sub("", d.entries[index].summary)
            feeds.append(Feed(title, link, source, time, summary))
        return feeds

    def get_message(self):
        return '{} / {}\n{}'.format(self.source, self.time, self.summary)
