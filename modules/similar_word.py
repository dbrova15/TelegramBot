import difflib
import json

from transliterate import translit
import codecs

from modules.constats import city_name, country_cod

city_name_latin = translit(city_name, "ru", reversed=True)
country_cod_latin = translit(country_cod.upper(), "ru", reversed=True)

fileObj = codecs.open("data/city.list.json", "r", "utf_8_sig")
text = fileObj.read()
fileObj.close()
json_obj = json.loads(text)

country_list = list(set([i["country"] for i in json_obj]))

full = []


def get_coordinats_city(city_name, country_cod):
    print("START")
    for data in json_obj:
        if data["country"] == country_cod.upper():
            if data["name"] == city_name:
                print(data["coord"]["lat"], data["coord"]["lon"])
                return data["coord"]["lat"], data["coord"]["lon"]


def get_country_data(country_name):
    data_country = []
    for data in json_obj:
        if data["country"] == country_name:
            data_country.append(data["name"])

    return data_country


def search_similar(seq_obj, check_word):
    seq_obj.set_seq1(check_word)
    full.append((seq_obj.ratio(), check_word))
    return None


def similar2(arr, word):
    s = difflib.SequenceMatcher()
    full = []
    # for i in arr:
    s.set_seq2(word)
    for n in arr:
        s.set_seq1(n)
        full.append((s.ratio(), n))
        full.sort(reverse=True)

    return full


def similar_one(arr, word):
    # seq_obj = difflib.SequenceMatcher()

    # seq_obj.set_seq2(word)
    # with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
    #     [pool.submit(search_similar, seq_obj, check_word) for check_word in arr]

    # for check_word in arr:
    #     search_similar(seq_obj, check_word)
    full = similar2(arr, word)

    # full.sort(reverse=True)

    finish_citys = []
    for i in full:
        i = i[1]
        if i not in finish_citys:
            finish_citys.append(i)
        if len(finish_citys) == 10:
            break

    res_dict = {str(i): finish_citys[i] for i in range(len(finish_citys))}
    return res_dict


def search_city(country_cod, city_name):
    city_name_latin = translit(city_name, "ru", reversed=True)
    country_cod_latin = translit(country_cod.upper(), "ru", reversed=True)

    city_list = get_country_data(country_cod_latin)
    res_dict = similar_one(city_list, city_name_latin)
    # print(res_dict)
    return res_dict


# search_city(country_cod, city_name)
