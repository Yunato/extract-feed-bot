import unittest
from dao import Dao

class TestFeedParamDao(unittest.TestCase):

    def test_init_with_list(self):
        self.assertIsNotNone(Dao([{"name": "table_name", "param": "table_param"}]))

    def test_init_with_dict(self):
        args = {"name": "table_name", "param": "table_param"}
        self.dao = Dao(args)
        self.assertIsNotNone(self.dao)
        colnames = self.dao.get_column_names(args["name"])
        self.assertTrue(args["param"] in colnames)

    def test_init_with_int(self):
        with self.assertRaises(TypeError):
            Dao(0)

    def test_init_with_string(self):
        with self.assertRaises(TypeError):
            Dao("test")

    def test_init_with_int_in_list(self):
        with self.assertRaises(TypeError):
            Dao([0, 1, 2])

if __name__ == '__main__':
    unittest.main()

