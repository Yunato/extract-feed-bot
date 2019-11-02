import unittest
from run import get_feeds

class TestGetFeeds(unittest.TestCase):

    def test_get_feeds_with_correct_url(self):
        RSS_URL = 'https://gigazine.net/index.php?/news/rss_2.0/'
        actual = get_feeds(RSS_URL)
        self.assertNotEqual(len(actual), 0)
        
    def test_get_feeds_with_wrong_url(self):
        RSS_URL = ''
        with self.assertRaises(ValueError):
            actual = get_feeds(RSS_URL)


if __name__ == '__main__':
    unittest.main()
