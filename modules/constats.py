import socket

hostname = socket.gethostname()
# print(hostname)

if hostname == "MI-Bakz":
    DEBAG = True
else:
    DEBAG = False

print(DEBAG)

WHEATHER_NOW = "Погода сейчас"
WHEATHER_F_SHORT = "Прогноз на сегодня"
DETAL_WHEATHER = "Детальный прогноз на 24 часа"
SEND_LOCALION = "Отправить GPS-данные"
SEND_CITY = "Указать город"
CHEANGE_LOCATION = "Изменить свой город"
BACK = "Назад"
SUBSCRIPTION = "Подписаться на рассылку"

lang = "ru"
lat = "48.468317500000005"
lon = "35.00443"
zip = 49052
MAX_WORKERS = 50
STATUS = 0

city_name = "Днипро"
country_cod = "ua"

start_text = """Привет! Я бот для получения данных о погоде. Для начала мне нужно узнать твоё местоположение. Для этого нажми кнопку {} или {}.
""".format(
    SEND_LOCALION, SEND_CITY
)

not_location_text = """Нипишите ваше местоположение"""

set_city_text = """Отправте код вашей страны и город. Например: UA, Kiev"""
choose_city_text = "Введите номер вашего города из предложеного списка. Если Вашего города нет в списке отправте свои GPS-данные."
error_choise_city_text = "Введите корректные данные вашего местоположения. Например: UA, Kiev. Или отправьте свои GPS-данные"
end_set_city_text = "Спасибо. Теперь я знаю Ваше местоположение и могу предоставлять коректную информацию о погоде."
info_button = """Справка по меню:
{} - Получить данные о текущей погоде, 
{} - прогноз на текущий день или на завтра если уже поздний вечер, 
{} - прогноз на следуюзие 24 часа, {} - изменить Ваш город""".format(
    WHEATHER_NOW, WHEATHER_F_SHORT, DETAL_WHEATHER, CHEANGE_LOCATION
)
choose_type_set_city = "Выберете способ указания местоположения"
im_dont_undestent = "Я не понял :("
what_should_do = "Что мне делать?"
