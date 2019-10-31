import unittest
from run import getFeeds

class TestGetFeeds(unittest.TestCase):

    def test_getFeeds_with_correctURL(self):
        RSS_URL = 'https://gigazine.net/index.php?/news/rss_2.0/'
        actual = getFeeds(RSS_URL)
        self.assertNotEqual(len(actual), 0)
        
    def test_getFeeds_with_wrongURL(self):
        RSS_URL = ''
        with self.assertRaises(NameError):
            actual = getFeeds(RSS_URL)


if __name__ == '__main__':
    unittest.main()
