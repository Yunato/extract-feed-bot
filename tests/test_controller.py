import unittest
from bot.controller import Controller

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
        self.assertEqual(logs, "")
        self.controller.add_url(user1, url1)
        logs = self.controller.get_logs()
        self.assertTrue("Successful" in logs)
        self.controller.add_url(user2, url1)
        logs = self.controller.get_logs()
        self.assertTrue("Failed" in logs)
        
    def test_add_url(self):
        msg = self.controller.add_url(user1, url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.add_url(user2, url1)
        self.assertTrue("Failed" in msg)
        msg = self.controller.add_url(user2, url2)
        self.assertTrue("Successful" in msg)

    def test_add_keyword(self):
        msg = self.controller.add_keyword(user1, keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.add_keyword(user2, keyword1)
        self.assertTrue("Failed" in msg)
        msg = self.controller.add_keyword(user2, keyword2)
        self.assertTrue("Successful" in msg)

    def test_delete_url_with_index(self):
        msg = self.controller.add_url(user1, url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_index(user1, 0)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_index(user2, 0)
        self.assertTrue("Failed" in msg)

    def test_delete_keyword_with_index(self):
        msg = self.controller.add_keyword(user1, keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_index(user1, 0)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_index(user2, 0)
        self.assertTrue("Failed" in msg)

    def test_delete_url_with_param(self):
        msg = self.controller.add_url(user1, url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_param(user1, url1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_url_with_param(user2, url2)
        self.assertTrue("Failed" in msg)

    def test_delete_keyword_with_param(self):
        msg = self.controller.add_keyword(user1, keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_param(user1, keyword1)
        self.assertTrue("Successful" in msg)
        msg = self.controller.delete_keyword_with_param(user2, keyword2)
        self.assertTrue("Failed" in msg)

    def test_get_urls(self):
        self.controller.add_url(user1, url1)
        self.controller.add_url(user2, url2)
        msg = self.controller.get_urls()
        self.assertTrue(url1 in msg)
        self.assertTrue(url2 in msg)

    def test_get_keywords(self):
        self.controller.add_keyword(user1, keyword1)
        self.controller.add_keyword(user2, keyword2)
        msg = self.controller.get_keywords()
        self.assertTrue(keyword1 in msg)
        self.assertTrue(keyword2 in msg)




if __name__ == '__main__':
    unittest.main()

