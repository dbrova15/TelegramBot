from modules.base_config import db_session
from modules.helper import get_coord
from main import bot
from modules.models import Users
from modules.weather_api import get_short_forecast


def send_short_forecast(id_user):
    lat, lon = get_coord(id_user)
    data_forecast = get_short_forecast(lat, lon)
    bot.send_message(id_user, data_forecast, parse_mode="Markdown")


def delete_time_send():
    db_session.query(Users).update({"time_send_sub": None})
    db_session.commit()


def worker_sub():
    pass
