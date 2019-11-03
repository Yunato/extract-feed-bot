import psycopg2
import urllib.parse as urlparse
import os

class Dao:

    TABLE_INFO = [
            {"name": "urls",        "param":  "url"},
            {"name": "keywords",    "param":  "keyword"}
            ]

    def __init__(self):
        self.__con = self.__get_connection()
        for info in Dao.TABLE_INFO:
            if not self.__has_table(table_name=info["name"]):
                self.__create_table(table_info=info)
        
    @classmethod
    def __get_connection(self):
        url = os.environ.get("DATABASE_URL")
        return psycopg2.connect(url)

    def __has_table(self, table_name):
        with self.__con.cursor() as cur:
            cur.execute("SELECT * FROM information_schema.columns WHERE table_name = %s;", (table_name,))
            rtn = bool(cur.rowcount)
        return rtn

    def __create_table(self, table_info):
        table_name = table_info["name"]
        table_param = table_info["param"]
        with self.__con.cursor() as cur:
            cur.execute(f"CREATE TABLE {table_name} (id serial PRIMARY KEY, {table_param} varchar);")

    def __get_count(self, table_name):
        with self.__con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name};")
            rtn = cur.rowcount
        return rtn

    def add_url(self, url):
        info = Dao.TABLE_INFO[0]
        table_name = info["name"]
        table_param = info["param"]
        with self.__con.cursor() as cur:
            cur.execute(f"INSERT INTO {table_name} ({table_param}) VALUES (%s);", (url,))

    def add_keyword(self, keyword):
        info = Dao.TABLE_INFO[1]
        table_name = info["name"]
        table_param = info["param"]
        with self.__con.cursor() as cur:
            cur.execute(f"INSERT INTO {table_name} ({table_param}) VALUES (%s);", (keyword,))

    def get_urls(self):
        return self.__get_count(Dao.TABLE_INFO[0]["name"])

    def get_keywords(self):
        return self.__get_count(Dao.TABLE_INFO[1]["name"])

