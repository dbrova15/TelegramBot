import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from modules.constats import DEBAG, BASE_DIR
from local_settings import DATABASE_URL

basedir = os.path.abspath(os.path.dirname(__file__))  # .replace("\\", "/")
project_dir = basedir.replace("\\", "/").split("/")[-2]
print(os.path.join(BASE_DIR, 'base.db'))
# DEBAG = False
if DEBAG:
    engine = create_engine("sqlite:///{}".format(os.path.join(BASE_DIR, 'base.db')))
else:
    engine = create_engine(
        DATABASE_URL,
        encoding="utf8",
        pool_recycle=280,
        pool_size=100,
        pool_pre_ping=True,
    )


session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)

Base = declarative_base()
Base.query = db_session.query_property()
