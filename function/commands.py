from database import base
from config import DB_host, DB_user , DB_password, DB_name


class Commands:
    def __init__(self):
        self.db= base.DataBase(
            host=DB_host,
            user=DB_user,
            password=DB_password,
            database=DB_name
        )
    def group_exist(self, chat_id):
        resalt=self.db.featch(f"SELECT COUNT(*) FROM groups WHERE chat_id= {chat_id}")[0][0]
        return bool(resalt)
    def add_group(self, msg):
        self.db.execute(f"INSERT INTO groups(chat_id, name) VALUES({msg.chat.id}, '{msg.chat.title}')")