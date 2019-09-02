import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from modules.constats import DEBAG
from local_settings import DATABASE_URL

basedir = os.path.abspath(os.path.dirname(__file__))  # .replace("\\", "/")
project_dir = basedir.replace("\\", "/").split("/")[-2]

# DEBAG = False
if DEBAG:
    engine = create_engine("sqlite:///../base.db")
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
