import datetime

from modules.constats import lon, lat
from modules.weather_api import request_weather, url_forecast


def create_forecast_data(data):
    list_data = []
    timezone = data["city"]["timezone"]
    place = data["city"]["name"] + ", " + data["city"]["country"]
    list_data.append(place)

    for row in data["list"]:
        date_time_str = row["dt_txt"]
        dt_txt = (
            datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
            + datetime.timedelta(seconds=timezone)
        ).strftime("%d-%m-%Y, %H:%M:%S")
        weather_type = row["weather"][0]["description"]
        temp = row["main"]["temp"]
        pressure = row["main"]["pressure"]
        wind_speed = row["wind"]["speed"]

        data_str = """\nВремя: {dt_txt},\nПогода: {weather_type},\nТ
        емпература: {temp} °C,\n
        Атмосферное давление: {pressure} hPa,\n
        Скорость ветра: {wind_speed} м/с""".format(
            dt_txt=dt_txt,
            weather_type=weather_type,
            temp=temp,
            pressure=pressure,
            wind_speed=wind_speed,
        )
        list_data.append(data_str)
    return """;\n""".join(list_data)


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


def weather_today(data):
    list_data = []
    list_weather_type = []
    list_temp = []
    list_pressure = []
    list_wind_speed = []
    timezone = data["city"]["timezone"]
    place = data["city"]["name"] + ", " + data["city"]["country"]
    list_data.append(place)

    dt_txt_now = (
        datetime.datetime.utcnow() + datetime.timedelta(seconds=timezone)
    ).strftime("%d-%m-%Y")

    for row in data["list"]:
        date_time_str = row["dt_txt"]
        dt_txt = (
            datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
            + datetime.timedelta(seconds=timezone)
        ).strftime("%d-%m-%Y")
        # print(dt_txt_now, dt_txt)
        if dt_txt_now == dt_txt:
            weather_type = row["weather"][0]["description"]
            temp = row["main"]["temp"]
            pressure = row["main"]["pressure"]
            wind_speed = row["wind"]["speed"]

            list_weather_type.append(weather_type)
            list_temp.append(temp)
            list_pressure.append(pressure)
            list_wind_speed.append(wind_speed)

    max_temp = max(list_temp)
    min_temp = min(list_temp)

    max_pressure = max(list_pressure)
    min_pressure = min(list_pressure)

    max_wind_speed = max(list_wind_speed)
    min_wind_speed = min(list_wind_speed)

    if "дождь" in list_weather_type:
        weather_type = "дождь"
    elif "снег" in list_weather_type:
        weather_type = "снег"
    else:
        weather_type = most_common_object(list_weather_type)

    data_text = """Дата: {dt_txt_now},\nПогода: {weather_type},\nТемпераура {min_temp} - {max_temp} °C,\nАтмосферное давление: {min_pressure} - {max_pressure} hPa,\nСкорость ветра: {min_wind_speed} - {max_wind_speed} м/с""".format(
        dt_txt_now=dt_txt_now,
        weather_type=weather_type,
        min_temp=min_temp,
        max_temp=max_temp,
        min_pressure=min_pressure,
        max_pressure=max_pressure,
        min_wind_speed=min_wind_speed,
        max_wind_speed=max_wind_speed,
    )
    return data_text


def get_forecast(lat, lon):
    data = request_weather(url_forecast, lat, lon)
    # pprint(data)
    return weather_today(data)


if __name__ == "__main__":
    # get_weather_now(lat, lon)
    r = get_forecast(lat, lon)
    print(r)
