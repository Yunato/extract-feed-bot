import unittest
from dao import Dao

class TestDao(unittest.TestCase):

    def setUp(self):
        self.dao = Dao()

    def test_get_count(self):
        self.assertEqual(self.dao.get_urls(), 0)
        self.assertEqual(self.dao.get_keywords(), 0)

    def test_add_url(self):
        self.assertEqual(self.dao.get_urls(), 0)
        self.dao.add_url("https://gigazine.net/index.php?/news/rss_2.0/")
        self.dao.add_url("https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf")
        self.assertEqual(self.dao.get_urls(), 2)

    def test_add_keyword(self):
        self.assertEqual(self.dao.get_keywords(), 0)
        self.dao.add_keyword("Android")
        self.dao.add_keyword("iOS")
        self.assertEqual(self.dao.get_keywords(), 2)


if __name__ == '__main__':
    unittest.main()
