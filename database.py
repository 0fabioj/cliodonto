import os
from dotenv import load_dotenv
load_dotenv()
import peewee as pw

class Database:
    def __init__(self):
        super().__init__()
        self.db = pw.MySQLDatabase(os.getenv("DB_NAME"),
                      host=os.getenv("DB_HOST"),
                      port=int(os.getenv("DB_PORT")),
                      user=os.getenv("DB_USER"),
                      passwd=os.getenv("DB_PASSWD"))
