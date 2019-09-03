import datetime

from modules.base_config import db_session
from modules.helper import get_coord, update_time_time_send_sub, del_time_time_send_sub
from modules.models import Users
from modules.weather_api import get_short_forecast
from weatherbot.weather_bot import bot


def send_subscription_data(id_user):
    lat, lon = get_coord(id_user)
    data_forecast = get_short_forecast(lat, lon)
    bot.send_message(id_user, data_forecast, parse_mode="Markdown")


def delete_time_send():
    db_session.query(Users).update({"time_send_sub": None})
    db_session.commit()


def worker_sub():
    data = db_session.query(Users).all()

    for obj in data:

        print(obj.id_user)
        time_check = datetime.datetime.timestamp(
            datetime.datetime.now() + datetime.timedelta(minutes=5)
        )
        print(obj.subscription)
        if obj.time_send_sub:
            continue
        time_sub_user = datetime.datetime.timestamp(obj.subscription)
        print(time_sub_user, time_check)
        print(time_sub_user - time_check)
        if time_sub_user < time_check:
            print(True)
        send_subscription_data(obj.id_user)
        update_time_time_send_sub(obj.id_user)


def del_null_sub():
    data = db_session.query(Users).all()

    for obj in data:
        del_time_time_send_sub(obj.id_user)


worker_sub()

