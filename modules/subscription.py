import datetime

from modules.base_config import db_session
from modules.helper import get_coord
from modules.models import Users
from modules.weather_api import get_short_forecast
from weatherbot.weather_bot import bot


def send_short_forecast(id_user):
    lat, lon = get_coord(id_user)
    data_forecast = get_short_forecast(lat, lon)
    bot.send_message(id_user, data_forecast, parse_mode="Markdown")


def delete_time_send():
    db_session.query(Users).update({"time_send_sub": None})
    db_session.commit()


def worker_sub():
    time_now = datetime.datetime.now()
    data = db_session.query(Users).filter(Users.time_send_sub.is_(None)).all()

    for obj in data:
        print(obj.id_user)
        send_short_forecast(obj.id_user)


# worker_sub()

data = db_session.query(Users).filter(Users.time_send_sub.
                                      is_(None)).all()