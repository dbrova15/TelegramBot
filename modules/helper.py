import datetime
import json
import sqlite3
import sqlalchemy
from modules.base_config import db_session
from modules.models import Users


def tomorrow_date() -> datetime:
    return (datetime.datetime.now() + datetime.timedelta(days=1)).date()


def update_time_subscription(id_user: int, time_str: str) -> None:
    date_time = "{} {}".format(tomorrow_date(), time_str)
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")

    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"subscription": date_time}
    )
    db_session.commit()


# def update_time_time_send_sub(id_user: int) -> None:
#     date_time = datetime.datetime.now()  # "{} {}".format(tomorrow_date(), time_str)
#
#     db_session.query(Users).filter(Users.id_user == id_user).update(
#         {"time_send_sub": date_time}
#     )
#     db_session.commit()


def update_time_sub(id_user: int, time_sub_user: datetime) -> None:
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"subscription": time_sub_user + datetime.timedelta(hours=24)}
    )
    db_session.commit()


def dell_sub(id_user):
    db_session.query(Users).filter(Users.id_user == id_user).delete()
    db_session.commit()


# def del_time_time_send_sub(id_user: int) -> None:
#     db_session.query(Users).filter(Users.id_user == id_user).update(
#         {"time_send_sub": None}
#     )
#     db_session.commit()


def get_country_cod(id_user: int) -> str:
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if not data:
        return ""
    return data.country_cod


def update_city(id_user: int, city: str) -> None:
    db_session.query(Users).filter(Users.id_user == id_user).update({"city": city})
    db_session.commit()


def update_country_cod(id_user: int, country_cod: str) -> None:
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"country_cod": country_cod}
    )
    db_session.commit()


def add_coord(
    id_user: int, city: str, country_cod: str, lat: float, lon: float, timezone: int
) -> None:
    obj = Users(id_user, city, country_cod, lat, lon, timezone, None)
    db_session.add(obj)
    try:
        db_session.commit()
    except sqlite3.IntegrityError:
        db_session.rollback()
        db_session.close()
        update_coord(id_user, city, country_cod, lat, lon, timezone)
    except sqlalchemy.exc.IntegrityError:
        db_session.rollback()
        db_session.close()
        update_coord(id_user, city, country_cod, lat, lon, timezone)


def update_coord(
    id_user: int, city: str, country_cod: str, lat: float, lon: float, timezone: int
) -> None:
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {
            "city": city,
            "country_cod": country_cod,
            "lat": lat,
            "lon": lon,
            "timezone": timezone,
        }
    )
    db_session.commit()


# принимаем ID пользователя: 123, получаем True
def chech_locate_null_foo(id_user: int) -> bool:
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if not data:
        return False
    return data.chech_locate_null()


# принимаем ID пользователя: 123, получаем {"city": "Dnipro", "lat": 48.450001, "lon": 34.98333}
def get_location_data_foo(id_user: int) -> dict:
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    data_location = data.get_data_location()
    return data_location


# принимаем ID пользователя: 123, получяем координаты пользователя 48.450001, 34.98333
def get_coord(id_user: int) -> tuple:
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    return data.lat, data.lon


def add_or_update_coord(
    id_user: int, city: str, country_cod: str, lat: float, lon: float, timezone: int
) -> None:
    if chech_locate_null_foo(id_user):
        update_coord(id_user, city, country_cod, lat, lon, timezone)
    else:
        add_coord(id_user, city, country_cod, lat, lon, timezone)


# def add_subscription_time(id_user: int, subscription_time):
#     db_session.query(Users).filter(Users.id_user == id_user).update(
#         {"subscription": subscription_time}
#     )
#     db_session.commit()


def updete_status(id_user: int, status: int) -> None:
    db_session.query(Users).filter(Users.id_user == id_user).update({"status": status})
    db_session.commit()


def get_status(id_user: int) -> None:
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if data:
        return data.status
    else:
        return None


def update_data_sity_dict(id_user: int, data_sity_dict: dict) -> None:
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"data_sity_dict": str(data_sity_dict)}
    )
    db_session.commit()


def get_data_sity_dict(id_user: int) -> dict:
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    data_sity_dict = json.loads(data.data_sity_dict.replace("'", '"'))
    return data_sity_dict


# add_or_update_coord(1, "Kiev", "UA", "2920", "283", :7000)
# print(get_status(1))data_sity_dict
