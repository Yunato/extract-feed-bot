import psycopg2
import datetime

from bot.dao import Dao

class LogDao(Dao):

    TABLE_INFO = {"name": "log", "param1":  "time", "param2": "who", "param3": "action", "param4": "object"}
    ACTION = ["ADD", "DELETE", "LIST", "FETCH"]
        
    def __init__(self):	
        super().__init__(LogDao.TABLE_INFO)

    def get_count(self, table_name):
        return super()._get_count(table_name)

    def __insert_action(self, user, action, msg):
        keys = list(LogDao.TABLE_INFO.keys())
        param = LogDao.TABLE_INFO[keys[1]]
        for index in range(len(keys) - 2):
            param += (", " + LogDao.TABLE_INFO[keys[index + 2]])
        with self._con.cursor() as cur:
            cur.execute(f"INSERT INTO {LogDao.TABLE_INFO['name']} ({param}) VALUES (%s, %s, %s, %s);",
                        (datetime.datetime.now(), user, action, msg))

    def insert_add_action(self, successful, user, content, dest):
        msg = "Successful " if successful else "Failed "
        msg += f"to add {content} to {dest}"
        self.__insert_action(user, LogDao.ACTION[0], msg)
        return msg

    def insert_delete_action(self, successful, user, content, src):
        msg = "Successful " if successful else "Failed "
        msg += f"to delete {content} from {src}"
        self.__insert_action(user, LogDao.ACTION[1], msg)
        return msg

    def insert_list_action(self, user, src):
        msg = f"Successful to get from {src}"
        self.__insert_action(user, LogDao.ACTION[2], msg)

    def insert_fetch_action(self, count):
        if count < 0:
            raise ValueError("The argument must be larger than 0.")
        msg = f"Successful to get {count} feeds"
        self.__insert_action("Bot", LogDao.ACTION[3], msg)

    def get_logs(self):
        table_name = LogDao.TABLE_INFO["name"]
        with self._con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name};")
            rtn = cur.fetchall()
        return rtn
