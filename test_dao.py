import unittest
from dao import Dao

class TestDao(unittest.TestCase):

    def setUp(self):
        self.dao = Dao()

    def test_get_count_with_no_table(self):
        self.assertEqual(self.dao.get_count(Dao.TABLE_INFO[0]["name"]), 0)

    def test_add_url(self):
        self.assertEqual(self.dao.get_count(Dao.TABLE_INFO[0]["name"]), 0)
        self.dao.add_url("https://gigazine.net/index.php?/news/rss_2.0/")
        self.dao.add_url("https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf")
        self.assertEqual(self.dao.get_count(Dao.TABLE_INFO[0]["name"]), 2)

if __name__ == '__main__':
    unittest.main()
