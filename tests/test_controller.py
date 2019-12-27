import unittest
from bot.controller import Controller
from bot.feed_dao import FeedDao

class TestController(unittest.TestCase):

    user1 = "Alice"
    user2 = "Bob"
    url1 = "https://gigazine.net/index.php?/news/rss_2.0/"
    url2 = "https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf"
    keyword1 = "android"
    keyword2 = "ios"

    def setUp(self):
        self.controller = Controller()

    def test_get_logs(self):
        logs = self.controller.get_logs()
        self.controller.add_url(self.user1, self.url1)
        logs = self.controller.get_logs()
        self.assertTrue("Successful" in logs)
        self.controller.add_url(self.user2, self.url1)
        logs = self.controller.get_logs()
        self.assertTrue("Failed" in logs)
        
    def test_add_url(self):
        msg = self.controller.add_url(self.user1, self.url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.add_url(self.user2, self.url1)
        self.assertTrue("Failed" in msg)
        msg = self.controller.add_url(self.user2, self.url2)
        self.assertTrue("Successful" in msg)

    def test_add_keyword(self):
        msg = self.controller.add_keyword(self.user1, self.keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.add_keyword(self.user2, self.keyword1)
        self.assertTrue("Failed" in msg)
        msg = self.controller.add_keyword(self.user2, self.keyword2)
        self.assertTrue("Successful" in msg)

    def test_delete_url_with_index(self):
        msg = self.controller.add_url(self.user1, self.url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_index(self.user1, 0)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_index(self.user2, 0)
        self.assertTrue("Failed" in msg)

    def test_delete_keyword_with_index(self):
        msg = self.controller.add_keyword(self.user1, self.keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_index(self.user1, 0)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_index(self.user2, 0)
        self.assertTrue("Failed" in msg)

    def test_delete_url_with_param(self):
        msg = self.controller.add_url(self.user1, self.url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_param(self.user1, self.url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_param(self.user2, self.url2)
        self.assertTrue("Failed" in msg)

    def test_delete_keyword_with_param(self):
        msg = self.controller.add_keyword(self.user1, self.keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_param(self.user1, self.keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_param(self.user2, self.keyword2)
        self.assertTrue("Failed" in msg)

    def test_get_urls(self):
        self.controller.add_url(self.user1, self.url1)
        self.controller.add_url(self.user2, self.url2)
        msg = self.controller.get_urls(self.user1)
        self.assertTrue(self.url1 in msg)
        self.assertTrue(self.url2 in msg)

    def test_get_keywords(self):
        self.controller.add_keyword(self.user1, self.keyword1)
        self.controller.add_keyword(self.user2, self.keyword2)
        msg = self.controller.get_keywords(self.user1)
        self.assertTrue(self.keyword1 in msg)
        self.assertTrue(self.keyword2 in msg)

    def test_fetch_feed(self):
        msg = self.controller.add_url(self.user1, self.url1)
        msg = self.controller.add_url(self.user2, self.url2)
        self.controller.fetch_feed()
        # self.assertFalse(self.controller.fetch_feed() == 0)

if __name__ == '__main__':
    unittest.main()

