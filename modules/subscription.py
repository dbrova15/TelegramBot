import datetime
import threading
import time

from modules.base_config import db_session
from modules.helper import update_time_sub
from modules.models import Users
from weatherbot.weather_bot import send_subscription_data


def worker_sub() -> None:
    data = db_session.query(Users).all()

    for obj in data:
        if obj.subscription is None:
            continue

        time_sub_user = datetime.datetime.timestamp(obj.subscription)

        if time.time() > time_sub_user:
            send_subscription_data(obj.id_user)
            update_time_sub(obj.id_user, obj.subscription)


# def del_null_sub():
#     data = db_session.query(Users).all()
#
#     for obj in data:
#         del_time_time_send_sub(obj.id_user)


def loop_worker() -> None:
    while True:
        worker_sub()
        time.sleep(60)


def thread_worker() -> None:
    e1 = threading.Event()
    t1 = threading.Thread(target=loop_worker)
    t1.start()
    e1.set()


if __name__ == "__main__":
    worker_sub()
