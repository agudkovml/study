import requests


# Задание №1,2
# Напишите функцию, которая возвращает название валюты (поле ‘Name’) с максимальным значением курса с помощью сервиса.
# Добавьте в класс Rate параметр diff, который в случае значения True в методах курсов валют будет возвращать изменение по сравнению в прошлым значением.
# Считайте, self.diff будет принимать значение True только при возврате значения курса. При отображении всей информации о валюте он не используется.

class Rate:
    def __init__(self, diff: bool = False):
        self.response = requests.get(
            "https://www.cbr-xml-daily.ru/daily_json.js"
        ).json()
        self.diff = bool(diff)

    def get_max_exchange_rate(self):
        valute_dict = self.response["Valute"]
        _, valute = max(valute_dict.items(), key=lambda item: item[1]["Value"])
        return valute["Name"], valute["Value"]

    def _get_value(self, code: str):
        currency = self.response["Valute"][code]
        if not self.diff:
            return currency["Value"]
        else:
            return currency["Value"] - currency["Previous"]

    def eur(self):
        return self._get_value("EUR")


# Test

test = Rate()
print(test.get_max_exchange_rate())
print(test.eur())
test.diff = True
print(test.eur())


# Задание №3
# Напишите класс Designer, который учитывает количество международных премий для дизайнеров
# Из презентации: "Повышение на 1 грейд за каждые 7 баллов. Получение международной премии – это +2 балла".
# Считайте, что при выходе на работу сотрудник уже имеет две премии и их количество не меняется со стажем (конечно если хотите это можно вручную менять)