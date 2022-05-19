# 使うタイプをimport
from sqlalchemy import Column, Integer, String, Text, DateTime
# modelsディレクトリにある database.py から db をimport
from models.database import db
from datetime import datetime



class onegaiContent(db) :
    # テーブル名
    __tablename__ = "onegaicontents"
    # カラム名 = Column(タイプ、オプション)
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(Datetime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None) :
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self) :
        return "<Title %r>" % (self.title)