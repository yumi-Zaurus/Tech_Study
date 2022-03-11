# 使うタイプをimport
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import cryptography

# MySQLに接続するための情報
engine = create_engine('mysql+pymysql://root:root@localhost/tech_study?charset=utf-8')
# オブジェクトを生成
db = declarative_base()

class Onegai(db):
    # テーブル名
    __tablename__ = "onegaicontents"
    # カラム名 = Column(タイプ、オプション)
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now)

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)


Session = sessionmaker(bind=engine)
db_session = Session()
db.metadate.create_all(engine)