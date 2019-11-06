import psycopg2
import urllib.parse as urlparse
import os

class Dao:
        
    def __init__(self, table_info):	
        self._con = self.__get_connection()	
        if type(table_info) is not list and type(table_info) is not dict:
            raise TypeError(f"The argument's type must be list or dict: {type(table_info)}")
        if type(table_info) is list and type(table_info[0]) is not dict:
            raise TypeError(f"The element's type in list must be dict: {type(table_info[0])}")
        if type(table_info) is dict:
            tmp = table_info
            table_info = [tmp]
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
        query_param = ""
        for key in table_info:
            if key == "name":
                continue
            if len(query_param) != 0:
                query_param += ","
            query_param += f" {table_info[key]} varchar"
        with self._con.cursor() as cur:
            cur.execute(f"CREATE TABLE {table_name} (id serial PRIMARY KEY, {query_param});")

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

    def get_column_names(self, table_name):
        with self._con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name}")
            return [col.name for col in cur.description]

