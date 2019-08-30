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
    pass
