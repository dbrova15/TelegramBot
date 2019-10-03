import sqlite3

import sqlalchemy

from modules.base_config import db_session
from modules.models import PR_modul


def add_pr_data(name, url, text, path_image):
    obj = PR_modul(name, url, text, path_image)
    db_session.add(obj)
    try:
        db_session.commit()
    except sqlite3.IntegrityError:
        db_session.rollback()
        db_session.close()
    except sqlalchemy.exc.IntegrityError:
        db_session.rollback()
        db_session.close()


def get_pr_data():
    pass


def del_pr_data():
    pass


def update_pr_data(name, url, text, path_image):
    db_session.query(PR_modul).filter(PR_modul.name == name).update(
        {"url": url, "text": text, "path_image": path_image}
    )
