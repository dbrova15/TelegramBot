import datetime

import requests
import json

from modules.constats import (
    lat,
    lon,
    lang,
    TEXT_WEATHER_TODAY,
    TEXT_WEATER_NOW,
    TEXT_WEATER_24,
    TEXT_WEATER_TOMORROW,
)
from modules.emoji import (
    getEmoji,
    snowflake,
    snowman,
    rain,
    thunderstorm,
    THERMOMETER,
    CLOCK,
    city_emoji,
    CALENDAR,
)
from local_settings import api_key_openweathermap
from modules.weather_req import check_weather_type

url_weather_now = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}&units=metric&lang={}"
url_forecast = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&APPID={}&units=metric&lang={}&cnt=10"


def weather_text_24(dt_txt, weather_type, emoji, req, temp):
    return TEXT_WEATER_24.format(
        CLOCK=CLOCK,
        dt_txt=dt_txt,
        weather_type=weather_type + " " + emoji,
        THERMOMETER=THERMOMETER,
        req=req,
        temp=temp,
    )


def weather_text_now(place, weather_type, emoji, req, temp):
    return TEXT_WEATER_NOW.format(
        place=place,
        city_emoji=city_emoji,
        weather_type=weather_type + " " + emoji,
        THERMOMETER=THERMOMETER,
        req=req,
        temp=temp,
    )


def weather_text_today(dt_txt_now, weather_type, emoji, req, min_temp, max_temp):
    return TEXT_WEATHER_TODAY.format(
        dt_txt_now=dt_txt_now,
        CALENDAR=CALENDAR,
        weather_type=weather_type + " " + emoji,
        THERMOMETER=THERMOMETER,
        req=req,
        min_temp=min_temp,
        max_temp=max_temp,
    )


def weather_text_tomorrow(dt_txt_now, weather_type, emoji, req, min_temp, max_temp):
    TEXT_WEATER_TOMORROW.format(
        dt_txt_now=dt_txt_now,
        weather_type=weather_type + " " + emoji,
        req=req,
        min_temp=min_temp,
        max_temp=max_temp,
    )


def create_weather_data(data):
    place = data["name"] + ", " + data["sys"]["country"]
    weather_id = data["weather"][0]["id"]
    weather_type = data["weather"][0]["description"]
    temp = data["main"]["temp"]

    req = check_weather_type(weather_type)
    emoji = getEmoji(weather_id)
    return weather_text_now(place, weather_type, emoji, req, temp)


def create_forecast_data(data):
    list_data = []
    timezone = data["city"]["timezone"]
    place = data["city"]["name"] + ", " + data["city"]["country"]
    list_data.append(place)
    for row in data["list"][:9]:
        date_time_str = row["dt_txt"]
        dt_txt = (
                datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
                + datetime.timedelta(seconds=timezone)
        ).strftime("%d.%m %H:%M")
        weather_id = row["weather"][0]["id"]
        weather_type = row["weather"][0]["description"]
        temp = row["main"]["temp"]

        req = check_weather_type(weather_type)
        emoji = getEmoji(weather_id)
        list_data.append(weather_text_24(dt_txt, weather_type, emoji, req, temp))
    print(len(list_data))
    return """\n""".join(list_data)


def most_common_object(list_obj):
    a_set = set(list_obj)

    most_common = None
    qty_most_common = 0

    for item in a_set:
        qty = list_obj.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    return most_common


def short_weather_today(data):
    # pprint(data)
    list_data = []
    list_weather_type = []
    list_weather_id = []
    list_temp = []
    timezone = data["city"]["timezone"]
    place = data["city"]["name"] + ", " + data["city"]["country"]
    list_data.append(place)

    dt_txt_now = (
            datetime.datetime.utcnow() + datetime.timedelta(seconds=timezone)
    ).strftime("%d.%m.%Y")

    for row in data["list"][:9]:
        dt_txt = datetime.datetime.strptime(
            row["dt_txt"], "%Y-%m-%d %H:%M:%S"
        ).strftime("%d.%m.%Y")
        if dt_txt_now == dt_txt:
            weather_id = row["weather"][0]["id"]
            weather_type = row["weather"][0]["description"]
            temp = row["main"]["temp"]

            list_weather_type.append(weather_type.lower())
            list_weather_id.append(weather_id)
            list_temp.append(temp)

    if len(list_temp) == 0:
        return None

    max_temp = max(list_temp)
    min_temp = min(list_temp)

    if "дождь" in list_weather_type:
        weather_type = "дождь"
        emoji = rain
    elif "гроза" in list_weather_type:
        weather_type = "гроза"
        emoji = thunderstorm
    elif "снег" in list_weather_type:
        weather_type = "снег"
        emoji = snowflake + " " + snowman
    else:
        weather_type = most_common_object(list_weather_type)
        weather_id = most_common_object(list_weather_id)
        emoji = getEmoji(weather_id)

    req = check_weather_type(weather_type)

    return weather_text_today(dt_txt_now, weather_type, emoji, req, min_temp, max_temp)


def short_weather_tomorrow(data):
    list_data = []
    list_weather_type = []
    list_weather_id = []
    list_temp = []
    timezone = data["city"]["timezone"]
    place = data["city"]["name"] + ", " + data["city"]["country"]
    list_data.append(place)

    dt_txt_now = (
            datetime.datetime.utcnow()
            + datetime.timedelta(seconds=timezone)
            + datetime.timedelta(days=1)
    ).strftime("%d-%m-%Y")

    for row in data["list"][:9]:
        weather_id = row["weather"][0]["id"]
        weather_type = row["weather"][0]["description"]
        temp = row["main"]["temp"]

        list_weather_type.append(weather_type)
        list_weather_id.append(weather_id)
        list_temp.append(temp)

    max_temp = max(list_temp)
    min_temp = min(list_temp)

    if "дождь" in list_weather_type:
        weather_type = "дождь"
        emoji = rain
    elif "гроза" in list_weather_type:
        weather_type = "гроза"
        emoji = thunderstorm
    elif "снег" in list_weather_type:
        weather_type = "снег"
        emoji = snowflake + " " + snowman
    else:
        weather_type = most_common_object(list_weather_type)
        weather_id = most_common_object(list_weather_id)
        emoji = getEmoji(weather_id)

    req = check_weather_type(weather_type)

    return weather_text_tomorrow(
        dt_txt_now, weather_type, emoji, req, min_temp, max_temp
    )


def request_weather(url, lat, lon):
    url = url.format(lat, lon, api_key_openweathermap, lang)
    response = requests.get(url)

    return json.loads(response.text)


def get_weather_now(lat, lon):
    data = request_weather(url_weather_now, lat, lon)
    return create_weather_data(data)


def get_forecast(lat, lon):
    data = request_weather(url_forecast, lat, lon)
    # print(data)
    return create_forecast_data(data)


def get_short_forecast(lat, lon):
    data = request_weather(url_forecast, lat, lon)

    r = short_weather_today(data)
    if not r:
        data_weather = get_weather_now(lat, lon)
        r = short_weather_tomorrow(data)
        return data_weather + "\n\n" + r
    return r


if __name__ == "__main__":
    # get_weather_now(lat, lon)
    r = get_forecast(lat, lon)
    print(r)
    # data = request_weather(url_forecast, lat, lon)
    # r = short_weather_tomorrow(data)
    # print(r)
