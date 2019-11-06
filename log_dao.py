import psycopg2
import datetime
import urllib.parse as urlparse
import os

from dao import Dao

class LogDao(Dao):

    TABLE_INFO = {"name": "log", "param1":  "time", "param2": "who", "param3": "action", "param4": "count"}
    ACTION = ["ADD", "DELETE", "LIST", "FETCH"]
        
    def __init__(self):	
        super().__init__(LogDao.TABLE_INFO)

    def get_count(self, table_name):
        return super()._get_count(table_name)

    def __insert_action(self, user, action, count):
        with self._con.cursor() as cur:
            cur.execute(f"INSERT INTO {LogDao.TABLE_INFO['name']} (time, who, action, count) VALUES (%s, %s, %s, %s);",
                        (datetime.datetime.now(), user, action, count))

    def insert_add_action(self, user):
        self.__insert_action(user, LogDao.ACTION[0], 0)

    def insert_delete_action(self, user):
        self.__insert_action(user, LogDao.ACTION[1], 0)

    def insert_list_action(self, user):
        self.__insert_action(user, LogDao.ACTION[2], 0)

    def insert_fetch_action(self, count):
        if count < 0:
            raise ValueError("The argument must be larger than 0.")
        self.__insert_action("bot", LogDao.ACTION[3], count)

    def get_logs(self):
        table_name = LogDao.TABLE_INFO["name"]
        with self._con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name};")
            rtn = cur.fetchall()
        return rtn
