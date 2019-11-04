import unittest
from feed_param_dao import FeedParamDao

class TestFeedParamDao(unittest.TestCase):

    def setUp(self):
        self.dao = FeedParamDao()

    def test_get_count(self):
        self.assertEqual(self.dao.get_count(FeedParamDao.TABLE_INFO[0]["name"]), 0)
        self.assertEqual(self.dao.get_count(FeedParamDao.TABLE_INFO[1]["name"]), 0)

    def test_add_url(self):
        self.assertEqual(self.dao.get_count(FeedParamDao.TABLE_INFO[0]["name"]), 0)
        self.dao.add_url("https://gigazine.net/index.php?/news/rss_2.0/")
        self.dao.add_url("https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf")
        self.assertEqual(self.dao.get_count(FeedParamDao.TABLE_INFO[0]["name"]), 2)

    def test_add_keyword(self):
        self.assertEqual(self.dao.get_count(FeedParamDao.TABLE_INFO[1]["name"]), 0)
        self.dao.add_keyword("android")
        self.dao.add_keyword("ios")
        self.assertEqual(self.dao.get_count(FeedParamDao.TABLE_INFO[1]["name"]), 2)

    def test_delete_url(self):
        self.assertFalse(self.dao.delete_url(0))

    def test_delete_keyword(self):
        self.assertFalse(self.dao.delete_keyword(0))


if __name__ == '__main__':
    unittest.main()
