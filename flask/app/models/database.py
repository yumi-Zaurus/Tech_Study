# 使うタイプをimport
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import cryptography
import os

# database.py と同じパスに、onegai.db というファイルを絶対パスで定義
database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'onegai.db')
# MySQLを利用して↑で定義した絶対パスにDBを構築
engine = create_engine('mysql+pymysql://root:root@localhost/tech_study?charset=utf-8' + database_file, convert_unicode=True)
# DB接続用インスタンスを生成
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()
# オブジェクトを生成
db = declarative_base()
# ↑で生成したオブジェクトにDBの情報を流し込む
db.query = db_session.query_property()



# DB初期化のための関数を定義
def init_db():
    import models.models                # DB初期化対象のテーブル定義を指定
    db.metadate.create_all(engine)      # テーブルを作成



