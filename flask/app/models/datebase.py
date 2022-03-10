from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# database.py と同じパスに、onegai.db というファイルを絶対パスで定義
database_file = os.path.join(os.path.abspath(os.path.dirnamt(__file__)), 'onegai.db')
engine = create_engine('sqlite:///')