import datetime
import difflib


def similar(arr):
    s = difflib.SequenceMatcher()
    full = []
    for i in arr:
        s.set_seq2(i)
        for n in (arr):
            if n == i:
                continue
            s.set_seq1(n)
            full.append((s.ratio(), n))
            full.sort(reverse=True)

    print("### Отладка ### Сколько каждое слово набрало очков похожести")
    for score, i in full:
        print(i + str(score))

    return full[0]


def similar2(arr, word):
    s = difflib.SequenceMatcher()
    full = []
    # for i in arr:
    s.set_seq2(word)
    for n in (arr):
        s.set_seq1(n)
        full.append((s.ratio(), n))
        full.sort(reverse=True)

    return full


# arr = ['голубец', 'конь', 'голубцы', 'лист', 'голубь']
# print(similar2(arr, 'голубь'))

# arr = ['стол', 'день', 'свет', 'клинок', 'светильник']
# print("Итоговый результат: " + similar(arr)[1])
#
# arr = ['восток', 'дань', 'исток', 'жир', 'голубь', 'да']
# print("Итоговый результат: " + similar(arr)[1])


# import json
# s2 = """{0: 'Dnepr', 1: 'Rudne', 2: 'Pridneprovsk', 3: 'Dnipro', 4: 'Vodyane', 5: 'Synevyr', 6: 'Nizhnedneprovsk', 7: 'Kudryne', 8: 'Horodne', 9: 'Vidradne'}"""
# s = "{1 : 'lolz', 2 : 'kitty'}"
# json_acceptable_string = s.replace("'", "\"")
# d = json.loads(json_acceptable_string)
# print(d)


# CLOSED_UMBRELLA
#
# bot.send_message(message.chat.id, end_set_city_text, reply_markup=keyboard, parse_mode="Markdown")

DATETIME_FORMAT_BASE = '%Y-%m-%d %H:%M'
#
# date = (datetime.datetime.now() + datetime.timedelta(
#     days=1)).date()
# time = "10:30"
# date_time = "{} {}".format(date, time)
# print(date_time)


import schedule
import time


def job():
    print("I'm working...")


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
