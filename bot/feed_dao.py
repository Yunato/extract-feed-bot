import psycopg2
import pytz
from datetime import datetime

from bot.dao import Dao
from bot.feed import Feed

class FeedDao(Dao):

    # TABLE_INFO = {"name": "feed", "param1":  "title", "param2": "link", "param3": "source", "param4": "time", "param5": "summary", "param6": "category"}
    TABLE_INFO = {"name": "feed", "param1":  "title", "param2": "link", "param3": "source", "param4": "time", "param5": "summary"}
        
    def __init__(self):	
        super().__init__(FeedDao.TABLE_INFO)
        print(self._con)

    def get_count(self):
        return super()._get_count(FeedDao.TABLE_INFO["name"])

    def add_feed(self, feed):
        keys = list(FeedDao.TABLE_INFO.keys())
        param = FeedDao.TABLE_INFO[keys[1]]
        for index in range(len(keys) - 2):
            param += (", " + FeedDao.TABLE_INFO[keys[index + 2]])
        with self._con.cursor() as cur:
            # cur.execute(f"INSERT INTO {FeedDao.TABLE_INFO['name']} ({param}) VALUES (%s, %s, %s, %s, %s, %s);",
                        # (feed.title, feed.link, feed.source, feed.time, feed.summary, feed.category))
            cur.execute(f"INSERT INTO {FeedDao.TABLE_INFO['name']} ({param}) VALUES (%s, %s, %s, %s, %s);",
                        (feed.title, feed.link, feed.source, feed.time, feed.summary))

    def get_feeds(self):
        with self._con.cursor() as cur:
            cur.execute(f"SELECT * FROM {FeedDao.TABLE_INFO['name']};")
            feeds = cur.fetchall()
        rtn = []
        for feed in feeds:
            title = feed[1]
            link = feed[2]
            source = feed[3]
            time = datetime.strptime(feed[4], '%Y/%m/%d %H:%M:%S')
            summary = feed[5]
            # category = feed[6]
            # rtn.append(Feed(title, link, source, time, summary, category))
            rtn.append(Feed(title, link, source, time, summary))
        return rtn

    def delete_all(self):
        with self._con.cursor() as cur:
            cur.execute(f"DELETE FROM {FeedDao.TABLE_INFO['name']}")

    def get_latest_time(self, src):
        with self._con.cursor() as cur:
            cur.execute(f"SELECT {FeedDao.TABLE_INFO['param4']} FROM {FeedDao.TABLE_INFO['name']} WHERE {FeedDao.TABLE_INFO['param3']} = %s ORDER BY id DESC LIMIT 1;", (src,))
            times = cur.fetchall()
            if(len(times) != 0):
                time = datetime.strptime(times[0][0], '%Y/%m/%d %H:%M:%S').replace(tzinfo=pytz.timezone("Asia/Tokyo"))
            else:
                time = datetime.min.replace(tzinfo=pytz.timezone("Asia/Tokyo"))
        return time
