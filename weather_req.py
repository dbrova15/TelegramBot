from emoji import CLOSED_UMBRELLA, warning_mark

REIN = "дождь"
LIGHT_RAIN = ""
SNOW = "снег"
LIGHT_SNOW = ""
HAIL = "град"


def check_weather_type(weather_type):
    if REIN in weather_type:
        req = "\n{}\n_Возьмите с собой зонт_ {}".format(
            "~{}~ ".format(warning_mark) * 5, CLOSED_UMBRELLA
        )
    else:
        req = ""
    return req
