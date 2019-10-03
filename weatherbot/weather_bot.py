import telebot

from modules.castom_keyboard import (
    start_keys,
    all_keys,
    chech_location,
    cheange_location_keys,
    time_subscription_mornirg,
    part_day_subscription,
)
from modules.constats import (
    start_text,
    not_location_text,
    DEBAG,
    WHEATHER_NOW,
    WHEATHER_F_SHORT,
    DETAL_WHEATHER,
    SEND_CITY,
    set_city_text,
    choose_city_text,
    end_set_city_text,
    error_choise_city_text,
    CHEANGE_LOCATION,
    choose_type_set_city,
    im_dont_undestent,
    BACK,
    what_should_do,
    SUBSCRIPTION,
    info_button,
)
from modules.helper import (
    chech_locate_null_foo,
    get_coord,
    updete_status,
    get_status,
    update_data_sity_dict,
    get_data_sity_dict,
    update_country_cod,
    get_country_cod,
    update_time_subscription,
    dell_sub,
)
from local_settings import api_key_test, api_key_tg

from modules.similar_word import search_city, get_coordinats_city


from modules.user_data import (
    update_location_user,
    get_location_dict,
    update_location_user_city,
)
from modules.weather_api import (
    get_weather_now,
    get_forecast,
    request_weather,
    url_weather_now,
    get_short_forecast,
)

if DEBAG:
    API = api_key_test
else:
    API = api_key_tg

bot = telebot.TeleBot(API)

STATUS = 0
data_sity_list = []
CHEANGE_LOCATION_MODE = False


def send_subscription_data(id_user) -> None:
    keyboard = all_keys()
    lat, lon = get_coord(id_user)
    data_forecast = get_short_forecast(lat, lon)
    try:
        bot.send_message(
            id_user, data_forecast, reply_markup=keyboard, parse_mode="Markdown"
        )
    except Exception as e:
        print(id_user)
        # print(e)
        if "Bad Request: chat not found" in str(e):
            print("Bad Request: chat not found")
            # from modules.subscription import dell_sub
            dell_sub(id_user)


def start_bot(message) -> None:
    if chech_locate_null_foo(message.chat.id):
        keyboard = all_keys()
    else:
        keyboard = chech_location(message)

    bot.send_message(message.chat.id, start_text)
    bot.send_message(
        message.chat.id, get_location_dict(message.chat.id), reply_markup=keyboard
    )
    # bot.send_message(message.chat.id, CLOSED_UMBRELLA, reply_markup=keyboard, parse_mode="Markdown")


@bot.message_handler(commands=["start"])
def start_message(message) -> None:
    if message.text == "/start":
        start_bot(message)


@bot.message_handler(content_types=["text"])
def send_text(message) -> None:
    print(message.text)
    print("status", get_status(message.chat.id))

    print(message.chat.id, type(message.chat.id))
    if get_status(message.chat.id) == 0:
        if chech_locate_null_foo(message.chat.id):
            keyboard = all_keys()

            if message.text.lower() == WHEATHER_NOW.lower():
                print(1)
                lat, lon = get_coord(message.chat.id)
                data_weather = get_weather_now(lat, lon)
                bot.send_message(
                    message.chat.id,
                    data_weather,
                    reply_markup=keyboard,
                    parse_mode="Markdown",
                )

            elif message.text.lower() == WHEATHER_F_SHORT.lower():
                print(2)
                lat, lon = get_coord(message.chat.id)
                data_forecast = get_short_forecast(lat, lon)
                bot.send_message(
                    message.chat.id,
                    data_forecast,
                    reply_markup=keyboard,
                    parse_mode="Markdown",
                )

            elif message.text.lower() == DETAL_WHEATHER.lower():
                print(3)
                lat, lon = get_coord(message.chat.id)
                data_forecast = get_forecast(lat, lon)
                bot.send_message(
                    message.chat.id,
                    data_forecast,
                    reply_markup=keyboard,
                    parse_mode="Markdown",
                )

            # elif message.text.lower() == SEND_CITY.lower():
            #     pass
            elif message.text.lower() == CHEANGE_LOCATION.lower():
                updete_status(message.chat.id, 1)
                keyboard = cheange_location_keys()
                bot.send_message(
                    message.chat.id,
                    choose_type_set_city,
                    reply_markup=keyboard,
                    parse_mode="Markdown",
                )
                pass
            elif message.text.lower() == SUBSCRIPTION.lower():
                # keyboard = time_subscription_hours()
                # keyboard = time_subscription_mornirg("6:00 - 12:00")
                keyboard = part_day_subscription()
                updete_status(message.chat.id, 4)
                bot.send_message(
                    message.chat.id,
                    "TEst",
                    reply_markup=keyboard,
                    parse_mode="Markdown",
                )
            else:
                print("else")
                pass

        else:
            print(7)
            keyboard = start_keys()
            bot.send_message(
                message.chat.id,
                not_location_text,
                reply_markup=keyboard,
                parse_mode="Markdown",
            )
    else:
        if message.text.lower() == SEND_CITY.lower():
            print(4)
            update_location_user_city(message, None, None, None, None)
            updete_status(message.chat.id, 2)
            bot.send_message(message.chat.id, set_city_text)
        else:
            if not get_status(message.chat.id):
                start_bot(message)
                return None
            elif message.text.lower() == BACK.lower():
                keyboard = all_keys()
                updete_status(message.chat.id, 0)
                bot.send_message(
                    message.chat.id,
                    what_should_do,
                    reply_markup=keyboard,
                    parse_mode="Markdown",
                )

            if get_status(message.chat.id) == 2:
                print("get data_city")
                data_city = message.text.split(",")

                if len(data_city) == 1:
                    data_city = message.text.split(" ")

                if len(data_city) != 2:
                    bot.send_message(
                        message.chat.id, error_choise_city_text, parse_mode="Markdown"
                    )
                else:
                    country_cod = data_city[0].strip().upper()
                    update_country_cod(message.chat.id, country_cod)

                    city_name = data_city[1].strip()
                    data_sity_dict = search_city(country_cod, city_name)
                    update_data_sity_dict(message.chat.id, data_sity_dict)
                    data_sity_list = "\n".join(
                        [
                            "{}: {}".format(i, data_sity_dict[i])
                            for i in data_sity_dict.keys()
                        ]
                    )
                    bot.send_message(message.chat.id, data_sity_list)
                    bot.send_message(message.chat.id, choose_city_text)
                    updete_status(message.chat.id, 3)

            elif get_status(message.chat.id) == 3:
                print("get city")
                try:
                    n_city = int(message.text)
                except Exception as e:
                    print(e)
                    bot.send_message(message.chat.id, im_dont_undestent)
                    return None

                data_sity_dict = get_data_sity_dict(message.chat.id)
                city_name = data_sity_dict[str(n_city)]

                country_cod = get_country_cod(message.chat.id)
                latitude, longitude = get_coordinats_city(city_name, country_cod)
                update_location_user_city(
                    message, city_name, country_cod, latitude, longitude
                )
                updete_status(message.chat.id, 0)
                keyboard = all_keys()
                bot.send_message(
                    message.chat.id,
                    end_set_city_text + "\n" + "=" * 30 + "\n" + info_button,
                    reply_markup=keyboard,
                    parse_mode="Markdown",
                )


@bot.message_handler(content_types=["location"])
def location_now(message) -> None:
    if message.location is not None:
        data = request_weather(
            url_weather_now, message.location.latitude, message.location.longitude
        )
        # print(data)
        update_location_user(message, data)

    if chech_locate_null_foo(message.chat.id):
        keyboard = all_keys()
    else:
        keyboard = chech_location(message)
    updete_status(message.chat.id, 0)
    bot.send_message(
        message.chat.id,
        get_location_dict(message.chat.id),
        reply_markup=keyboard,
        parse_mode="Markdown",
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call) -> None:
    if get_status(call.message.chat.id) == 4:
        keyboard = time_subscription_mornirg(call.data)
        updete_status(call.message.chat.id, 5)
        bot.send_message(
            call.message.chat.id, "axas", reply_markup=keyboard, parse_mode="Markdown"
        )
    elif get_status(call.message.chat.id) == 5:
        if len(call.data) != 5:

            keyboard = all_keys()
            bot.send_message(
                call.message.chat.id,
                "Test",
                reply_markup=keyboard,
                parse_mode="Markdown",
            )
        else:
            update_time_subscription(call.message.chat.id, call.data)
            updete_status(call.message.chat.id, 0)
            keyboard = all_keys()
            bot.send_message(
                call.message.chat.id,
                "Test",
                reply_markup=keyboard,
                parse_mode="Markdown",
            )


def weather_bot() -> None:
    # worker_sub()
    from modules.subscription import thread_worker

    thread_worker()
    bot.polling()


if __name__ == "__main__":
    weather_bot()
