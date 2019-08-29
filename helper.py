import datetime
import json
from base_config import db_session
from models import Users


def tomorrow_date():
    return (datetime.datetime.now() + datetime.timedelta(
        days=1)).date()


def get_time_subscription(id_user):
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if not data:
        return None
    return data.subscription


def update_time_subscription(id_user, time_str):
    date_time = "{} {}".format(tomorrow_date(), time_str)

    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"subscription": date_time})
    db_session.commit()


def get_country_cod(id_user):
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if not data:
        return None
    return data.country_cod


def update_city(id_user, city):
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"city": city})
    db_session.commit()


def update_country_cod(id_user, country_cod):
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"country_cod": country_cod})
    db_session.commit()


def add_coord(id_user, city, country_cod, lat, lon, timezone):
    obj = Users(id_user, city, country_cod, lat, lon, timezone, None)
    db_session.add(obj)
    db_session.commit()


def update_coord(id_user, city, country_cod, lat, lon, timezone):
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"city": city, "country_cod": country_cod, "lat": lat, "lon": lon, "timezone": timezone})
    db_session.commit()


def chech_locate_null_foo(id_user):
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if not data:
        return None
    return data.chech_locate_null()


def get_location_data_foo(id_user):
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    data_location = data.get_data_location()
    return data_location


def get_coord(id_user):
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    return data.lat, data.lon


def add_or_update_coord(id_user, city, country_cod, lat, lon, timezone):
    if chech_locate_null_foo(id_user):
        update_coord(id_user, city, country_cod, lat, lon, timezone)
    else:
        add_coord(id_user, city, country_cod, lat, lon, timezone)


def add_subscription_time(id_user, subscription_time):
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"subscription": subscription_time})
    db_session.commit()


def updete_status(id_user, status):
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"status": status})
    db_session.commit()


def get_status(id_user):
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if data:
        return data.status
    else:
        return None


def update_data_sity_dict(id_user, data_sity_dict):
    db_session.query(Users).filter(Users.id_user == id_user).update(
        {"data_sity_dict": data_sity_dict})
    db_session.commit()


def get_data_sity_dict(id_user):
    data = db_session.query(Users).filter(Users.id_user == id_user).first()
    if data.data_sity_dict:
        data_sity_dict = json.loads(data.data_sity_dict.replace("'", "\""))
        return data_sity_dict
    else:
        return None

# add_or_update_coord(1, "Kiev", "UA", "2920", "283", :7000)
# print(get_status(1))data_sity_dict
