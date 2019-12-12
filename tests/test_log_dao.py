import unittest
from bot.log_dao import LogDao
from bot.feed_param_dao import FeedParamDao

class TestLogDao(unittest.TestCase):

    user = "Alice"
    url = "https://gigazine.net/index.php?/news/rss_2.0/"

    def setUp(self):
        self.dao = LogDao()

    def test_insert_add_action(self):
        self.dao.insert_add_action(self.user, self.url, FeedParamDao.TABLE_INFO[0]["name"])
        logs = self.dao.get_logs()
        for log in logs:
            self.assertTrue(self.user in log)
            self.assertTrue(LogDao.ACTION[0] in log)
            self.assertTrue("0" in log)

    def test_insert_delete_action(self):
        self.dao.insert_delete_action(self.user, self.url, FeedParamDao.TABLE_INFO[0]["name"])
        logs = self.dao.get_logs()
        for log in logs:
            self.assertTrue(self.user in log)
            self.assertTrue(LogDao.ACTION[1] in log)
            self.assertTrue("0" in log)

    def test_insert_list_action(self):
        self.dao.insert_list_action(self.user, FeedParamDao.TABLE_INFO[0]["name"])
        logs = self.dao.get_logs()
        for log in logs:
            self.assertTrue(self.user in log)
            self.assertTrue(LogDao.ACTION[2] in log)
            self.assertTrue("0" in log)

    def test_insert_fetch_action(self):
        self.dao.insert_fetch_action(10)
        logs = self.dao.get_logs()
        for log in logs:
            self.assertTrue("bot" in log)
            self.assertTrue(LogDao.ACTION[3] in log)
            self.assertTrue("10" in log)

    def test_insert_fetch_action_with_negative_argument(self):
        with self.assertRaises(ValueError):
            self.dao.insert_fetch_action(-10)


if __name__ == '__main__':
    unittest.main()
