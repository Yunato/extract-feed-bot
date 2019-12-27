import json
import pytz
import math
import random
from datetime import datetime
from bot.feed import Feed
from bot.feed_dao import FeedDao
from bot.feed_param_dao import FeedParamDao
from bot.log_dao import LogDao

class Controller:
        
    def __init__(self):	
        self.feed_dao = FeedDao()
        self.feed_param_dao = FeedParamDao()
        self.log_dao = LogDao()

    def add_url(self, user, url):
        successful = self.feed_param_dao.add_url(url)
        msg = self.log_dao.insert_add_action(successful, user, url, FeedParamDao.TABLE_INFO[0]["name"]) 
        return msg

    def add_keyword(self, user, keyword):
        successful = self.feed_param_dao.add_keyword(keyword)
        msg = self.log_dao.insert_add_action(successful, user, keyword, FeedParamDao.TABLE_INFO[1]["name"])
        return msg

    def get_urls(self, user):
        msg = ""
        urls = self.feed_param_dao.get_urls()
        self.log_dao.insert_list_action(user, FeedParamDao.TABLE_INFO[0]["name"])
        for index in range(len(urls)):
            msg += f"{index}: {urls[index]}\n"
        return msg

    def get_keywords(self, user):
        msg = ""
        keywords = self.feed_param_dao.get_keywords()
        self.log_dao.insert_list_action(user, FeedParamDao.TABLE_INFO[1]["name"])
        for index in range(len(keywords)):
            msg += f"{index}: {keywords[index]}\n"
        return msg

    def delete_url_with_param(self, user, url):
        successful = self.feed_param_dao.delete_url_with_param(url)
        msg = self.log_dao.insert_delete_action(successful, user, url, FeedParamDao.TABLE_INFO[0]["name"])
        return msg

    def delete_keyword_with_param(self, user, keyword):
        successful = self.feed_param_dao.delete_keyword_with_param(keyword)
        msg = self.log_dao.insert_delete_action(successful, user, keyword, FeedParamDao.TABLE_INFO[1]["name"])
        return msg

    def delete_url_with_index(self, user, index):
        urls = self.feed_param_dao.get_urls()
        url = urls[index] if 0 <= index and index < len(urls) else "INVALID URL"
        successful = self.feed_param_dao.delete_url_with_index(index)
        msg = self.log_dao.insert_delete_action(successful, user, url, FeedParamDao.TABLE_INFO[0]["name"])
        return msg

    def delete_keyword_with_index(self, user, index):
        keywords = self.feed_param_dao.get_keywords()
        keyword = keywords[index] if 0 <= index and index < len(keywords) else "INVALID KEYWORD"
        successful = self.feed_param_dao.delete_keyword_with_index(index)
        msg = self.log_dao.insert_delete_action(successful, user, keyword, FeedParamDao.TABLE_INFO[1]["name"])
        return msg

    def get_logs(self, count = 10):
        msg = ""
        logs = self.log_dao.get_logs()
        length = count if count <= len(logs) else len(logs)
        for index in range(length):
            log = logs[index]
            msg += f"{log[1]}: [{log[3]}] {log[4]} by {log[2]}\n"
        return msg

    def fetch_feed(self):
        new_feeds = []
        urls = self.feed_param_dao.get_urls()
        keywords = self.feed_param_dao.get_keywords()
        for url in urls:
            feeds = Feed.fetch_feed(url)
            if len(feeds) == 0:
                continue
            latest_time = self.feed_dao.get_latest_time(feeds[0].source)
            for feed in feeds:
                time = datetime.strptime(feed.time, '%Y/%m/%d %H:%M:%S').replace(tzinfo=pytz.timezone("Asia/Tokyo"))
                if time <= latest_time:
                    feeds.remove(feed)
                isIncluded = False
                for keyword in keywords:
                    if keyword in feed.summary:
                        isIncluded = True
                if not isIncluded:
                    feeds.remove(feed)
            new_feeds.extend(feeds)
        for feed in new_feeds:
            self.feed_dao.add_feed(feed)
        self.log_dao.insert_fetch_action(len(new_feeds))
        return self.feed_dao.get_count()

    def create_message(self):
        message = {}
        message['attachments'] = []
        attachments = []
        for feed in self.feed_dao.get_feeds():
            attachment = {}
            num = 0
            for c in feed.source:
                num += ord(c)
            random.seed(num)
            attachment['title'] = feed.title
            attachment['title_link'] = feed.link
            attachment['text'] = feed.get_message()
            attachment['color'] = "#" + hex(math.floor(random.random() * 16777215))
            attachments.append(attachment)
        if(len(attachments) == 0):
            attachment = {}
            attachment['title'] = 'No feed for today.'
            attachments.append(attachment)
        message['attachments'].extend(attachments)
        return json.dumps(message).encode()



