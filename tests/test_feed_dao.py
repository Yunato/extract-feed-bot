import unittest
import pytz 
from bot.feed_dao import FeedDao
from bot.feed import Feed
from datetime import datetime, timedelta

class TestFeedDao(unittest.TestCase):

    feed_info1 = ["title1", "link1", "src1", datetime.now().astimezone(pytz.timezone("Asia/Tokyo")), "summary1", "category1"]
    feed_info2 = ["title2", "link2", "src2", datetime.now().astimezone(pytz.timezone("Asia/Tokyo")), "summary2", "category2"]

    def setUp(self):
        self.dao = FeedDao()

    def test_add_feed(self):
        self.assertEqual(self.dao.get_count(), 0)
        self.dao.add_feed(Feed(self.feed_info1[0], self.feed_info1[1], self.feed_info1[2], self.feed_info1[3], self.feed_info1[4], self.feed_info1[5]))
        self.dao.add_feed(Feed(self.feed_info2[0], self.feed_info2[1], self.feed_info2[2], self.feed_info2[3], self.feed_info2[4], self.feed_info2[5]))
        self.assertEqual(self.dao.get_count(), 2)

    def test_get_feeds(self):
        self.assertEqual(self.dao.get_count(), 0)
        self.dao.add_feed(Feed(self.feed_info1[0], self.feed_info1[1], self.feed_info1[2], self.feed_info1[3], self.feed_info1[4], self.feed_info1[5]))
        self.dao.add_feed(Feed(self.feed_info2[0], self.feed_info2[1], self.feed_info2[2], self.feed_info2[3], self.feed_info2[4], self.feed_info2[5]))
        self.assertEqual(self.dao.get_count(), 2)
        feeds = self.dao.get_feeds()
        self.assertEqual(len(feeds), 2)

    def test_delete_all(self):
        self.assertEqual(self.dao.get_count(), 0)
        self.dao.add_feed(Feed(self.feed_info1[0], self.feed_info1[1], self.feed_info1[2], self.feed_info1[3], self.feed_info1[4], self.feed_info1[5]))
        self.dao.add_feed(Feed(self.feed_info2[0], self.feed_info2[1], self.feed_info2[2], self.feed_info2[3], self.feed_info2[4], self.feed_info2[5]))
        self.assertEqual(self.dao.get_count(), 2)
        self.dao.delete_all()
        self.assertEqual(self.dao.get_count(), 0)

    def test_get_latest_time(self):
        self.assertEqual(self.dao.get_count(), 0)
        self.dao.add_feed(Feed(self.feed_info1[0], self.feed_info1[1], self.feed_info1[2], self.feed_info1[3], self.feed_info1[4], self.feed_info1[5]))
        self.dao.add_feed(Feed(self.feed_info2[0], self.feed_info2[1], self.feed_info2[2], self.feed_info2[3], self.feed_info2[4], self.feed_info2[5]))
        self.assertEqual(self.dao.get_count(), 2)
        self.assertTrue(self.dao.get_latest_time(self.feed_info2[2]) <= self.feed_info2[3])
        self.assertTrue(self.dao.get_latest_time(self.feed_info2[2]) > self.feed_info2[3] - timedelta(days=1))
