import telebot
from datetime import datetime, timedelta
from telebot import types

from modules.constats import (
    WHEATHER_NOW,
    WHEATHER_F_SHORT,
    DETAL_WHEATHER,
    SEND_CITY,
    SEND_LOCALION,
    BACK,
    CHEANGE_LOCATION,
)
from modules.user_data import data_location


def part_day_subscription():
    keyboard = types.InlineKeyboardMarkup()

    keyboard.row(
        types.InlineKeyboardButton(
            text=str("6:00 - 12:00"), callback_data=str("6:00 - 12:00")
        )
    )
    keyboard.row(
        types.InlineKeyboardButton(
            text=str("12:00 - 18:00"), callback_data=str("12:00 - 18:00")
        )
    )
    keyboard.row(
        types.InlineKeyboardButton(
            text=str("18:00 - 00:00"), callback_data=str("18:00 - 00:00")
        )
    )
    keyboard.row(
        types.InlineKeyboardButton(
            text=str("00:00 - 6:00"), callback_data=str("00:00 - 6:00")
        )
    )

    return keyboard


"""    dt_txt_now = (datetime.datetime.utcnow() + datetime.timedelta(
        seconds=timezone) + datetime.timedelta(
        days=1)).strftime("%d-%m-%Y")
        """


def time_subscription_mornirg(date_string):
    keyboard = types.InlineKeyboardMarkup()
    list_time = date_string.split(" - ")
    time_list = []
    start_time = datetime.strptime(list_time[0], "%H:%M")

    for i in range(24):
        dt_txt = start_time + timedelta(minutes=15)
        start_time = dt_txt
        time_list.append(
            types.InlineKeyboardButton(
                text=str(dt_txt.strftime("%H:%M")),
                callback_data=str(dt_txt.strftime("%H:%M")),
            )
        )

    keyboard.row(*time_list[0:6])
    keyboard.row(*time_list[6:12])
    keyboard.row(*time_list[12:18])
    keyboard.row(*time_list[18:24])
    keyboard.row(types.InlineKeyboardButton(text=str(BACK), callback_data=str(BACK)))
    return keyboard


def time_subscription_hours():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        *[
            types.InlineKeyboardButton(text=str(name), callback_data=str(name))
            for name in range(0, 6)
        ]
    )
    keyboard.row(
        *[
            types.InlineKeyboardButton(text=str(name), callback_data=str(name))
            for name in range(6, 12)
        ]
    )
    keyboard.row(
        *[
            types.InlineKeyboardButton(text=str(name), callback_data=str(name))
            for name in range(12, 18)
        ]
    )
    keyboard.row(
        *[
            types.InlineKeyboardButton(text=str(name), callback_data=str(name))
            for name in range(18, 24)
        ]
    )

    # keyboard.row(BACK)
    return keyboard


def time_subscription_minuts():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        *[
            types.InlineKeyboardButton(text=name, callback_data=name)
            for name in [00, 5, 10, 15]
        ]
    )
    keyboard.add(
        *[
            types.InlineKeyboardButton(text=name, callback_data=name)
            for name in [20, 25, 30, 35]
        ]
    )
    keyboard.add(
        *[
            types.InlineKeyboardButton(text=name, callback_data=name)
            for name in [40, 45, 50, 55]
        ]
    )
    # keyboard.row(BACK)
    return keyboard


def chech_location(message):
    if data_location.setdefault(message.chat.id):
        keyboard = all_keys()
    else:
        keyboard = start_keys()
    return keyboard


def all_keys():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(WHEATHER_NOW, WHEATHER_F_SHORT)
    keyboard.row(DETAL_WHEATHER, CHEANGE_LOCATION)
    # keyboard.row(SUBSCRIPTION)

    # button_geo = types.KeyboardButton(text=SEND_LOCALION, request_location=True)
    # keyboard.add(button_geo)
    return keyboard


def start_keys():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(SEND_CITY)
    button_geo = types.KeyboardButton(text=SEND_LOCALION, request_location=True)
    keyboard.add(button_geo)
    return keyboard


def cheange_location_keys():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(SEND_CITY)
    button_geo = types.KeyboardButton(text=SEND_LOCALION, request_location=True)
    keyboard.add(button_geo)
    keyboard.row(BACK)
    return keyboard
