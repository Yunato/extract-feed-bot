import psycopg2
import urllib.parse as urlparse
import os

class Dao:
        
    def __init__(self, table_info):	
        self._con = self.__get_connection()	
        for info in table_info:	
            if not self.__has_table(table_name=info["name"]):	
                self.__create_table(table_info=info)

    def __get_connection(self):
        url = os.environ.get("DATABASE_URL")
        return psycopg2.connect(url)

    def __has_table(self, table_name):
        with self._con.cursor() as cur:
            cur.execute("SELECT * FROM information_schema.columns WHERE table_name = %s;", (table_name,))
            rtn = bool(cur.rowcount)
        return rtn

    def __create_table(self, table_info):
        table_name = table_info["name"]
        table_param = table_info["param"]
        with self._con.cursor() as cur:
            cur.execute(f"CREATE TABLE {table_name} (id serial PRIMARY KEY, {table_param} varchar);")

    def _get_count(self, table_name):
        with self._con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name};")
            rtn = cur.rowcount
        return rtn

    def _delete(self, table_name, index):
        count = 0
        with self._con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name} WHERE id = %s;", (index,))
            count = cur.rowcount
        if count == 0:
            return False
        with self._con.cursor() as cur:
            cur.execute(f"DELETE FROM {table_name} WHERE id = {index};")
            return True

