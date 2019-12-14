import psycopg2
import urllib.parse as urlparse
import os

from bot.dao import Dao

class FeedParamDao(Dao):

    TABLE_INFO = [
            {"name": "urls",        "param":  "url"}, 
            {"name": "keywords",    "param":  "keyword"} 
            ] 
        
    def __init__(self):	
        super().__init__(FeedParamDao.TABLE_INFO)

    def get_count(self, table_name):
        return super()._get_count(table_name)

    def add_url(self, url):
        urls = self.get_urls()
        for saved_url in urls:
            if (url in saved_url):
                return False
        info = FeedParamDao.TABLE_INFO[0]
        table_name = info["name"]
        table_param = info["param"]
        with self._con.cursor() as cur:
            cur.execute(f"INSERT INTO {table_name} ({table_param}) VALUES (%s);", (url,))
        return True

    def add_keyword(self, keyword):
        keywords = self.get_keywords()
        for saved_keyword in keywords:
            if (keyword in saved_keyword):
                return False
        info = FeedParamDao.TABLE_INFO[1]
        table_name = info["name"]
        table_param = info["param"]
        with self._con.cursor() as cur:
            cur.execute(f"INSERT INTO {table_name} ({table_param}) VALUES (%s);", (keyword,))
        return True

    def get_urls(self):
        info = FeedParamDao.TABLE_INFO[0]
        table_name = info["name"]
        param = info["param"]
        with self._con.cursor() as cur:
            cur.execute(f"SELECT {param} FROM {table_name};")
            rtn = cur.fetchall()
        return rtn

    def get_keywords(self):
        info = FeedParamDao.TABLE_INFO[1]
        table_name = info["name"]
        param = info["param"]
        with self._con.cursor() as cur:
            cur.execute(f"SELECT {param} FROM {table_name};")
            rtn = cur.fetchall()
        return rtn

    # Called from delete_url_with_param, delete_keyword_with_param
    def _delete_with_param(self, param, params, func):
        for index in range(len(params)):
            if (param in params[index]):
                return func(index)
        return False

    def delete_url_with_param(self, url):
        urls = self.get_urls()
        return self._delete_with_param(url, urls, self.delete_url_with_index)

    def delete_keyword_with_param(self, keyword):
        keywords = self.get_keywords()
        return self._delete_with_param(keyword, keywords, self.delete_keyword_with_index)

    def delete_url_with_index(self, index):
        return super()._delete(FeedParamDao.TABLE_INFO[0]["name"], index)

    def delete_keyword_with_index(self, index):
        return super()._delete(FeedParamDao.TABLE_INFO[1]["name"], index)

