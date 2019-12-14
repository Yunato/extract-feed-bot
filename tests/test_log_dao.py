import unittest
from bot.log_dao import LogDao
from bot.feed_param_dao import FeedParamDao

class TestLogDao(unittest.TestCase):

    user1 = "Alice"
    user2 = "Bob"
    url1 = "https://gigazine.net/index.php?/news/rss_2.0/"
    url2 = "https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf"

    def setUp(self):
        self.dao = LogDao()

    def test_insert_add_action(self):
        self.dao.insert_add_action(True, self.user1, self.url1, FeedParamDao.TABLE_INFO[0]["name"])
        self.dao.insert_add_action(False, self.user2, self.url2, FeedParamDao.TABLE_INFO[0]["name"])
        logs = self.dao.get_logs()
        print(logs)
        self.assertTrue(self.user1 in logs[0][2])
        self.assertTrue(LogDao.ACTION[0] in logs[0][3])
        self.assertTrue("Successful" in logs[0][4])
        self.assertTrue(self.user2 in logs[1][2])
        self.assertTrue(LogDao.ACTION[0] in logs[1][3])
        self.assertTrue("Failed" in logs[1][4])

    def test_insert_delete_action(self):
        self.dao.insert_delete_action(True, self.user1, self.url1, FeedParamDao.TABLE_INFO[0]["name"])
        self.dao.insert_delete_action(False, self.user2, self.url2, FeedParamDao.TABLE_INFO[0]["name"])
        logs = self.dao.get_logs()
        print(logs)
        self.assertTrue(self.user1 in logs[0][2])
        self.assertTrue(LogDao.ACTION[1] in logs[0][3])
        self.assertTrue("Successful" in logs[0][4])
        self.assertTrue(self.user2 in logs[1][2])
        self.assertTrue(LogDao.ACTION[1] in logs[1][3])
        self.assertTrue("Failed" in logs[1][4])

    def test_insert_list_action(self):
        self.dao.insert_list_action(self.user1, FeedParamDao.TABLE_INFO[0]["name"])
        logs = self.dao.get_logs()
        print(logs)
        self.assertTrue(self.user1 in logs[0][2])
        self.assertTrue(LogDao.ACTION[2] in logs[0][3])
        self.assertTrue("Successful" in logs[0][4])

    def test_insert_fetch_action(self):
        self.dao.insert_fetch_action(10)
        logs = self.dao.get_logs()
        print(logs)
        self.assertTrue("Bot" in logs[0][2])
        self.assertTrue(LogDao.ACTION[3] in logs[0][3])
        self.assertTrue("Successful" in logs[0][4])

    def test_insert_fetch_action_with_negative_argument(self):
        with self.assertRaises(ValueError):
            self.dao.insert_fetch_action(-10)


if __name__ == '__main__':
    unittest.main()
