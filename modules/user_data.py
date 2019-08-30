from modules.base_config import db_session
from modules.helper import (
    add_or_update_coord,
    chech_locate_null_foo,
    get_location_data_foo,
)
from modules.models import Users

data_location = {}


def get_location_dict(chat_id):

    if chech_locate_null_foo(chat_id):
        data_location = get_location_data_foo(chat_id)
        lat = data_location["lat"]
        lon = data_location["lon"]
        city = data_location["city"]
        data = "Широта: {}, долгота {}\nГород: {}".format(lat, lon, city)
    else:
        data = "Я ешё не знаю твоего местоположения"
    return data


def update_location_user(message, data):

    add_or_update_coord(
        message.chat.id,
        data["name"],
        data["sys"]["country"],
        message.location.latitude,
        message.location.longitude,
        None,
    )


def update_location_user_city(message, city_name, country_name, latitude, longitude):
    add_or_update_coord(
        message.chat.id, city_name, country_name, latitude, longitude, None
    )


def update_city_user(id_user, city):
    db_session.query(Users).filter(Users.id_user == id_user).update({"city": city})
    db_session.commit()
