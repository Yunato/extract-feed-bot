import unittest
from dao import Dao

class TestDao(unittest.TestCase):

    def setUp(self):
        self.dao = Dao()

    def test_get_count(self):
        self.assertNotEqual(self.dao.get_count(Dao.TABLE_INFO[0]["name"]), 0)


if __name__ == '__main__':
    unittest.main()
