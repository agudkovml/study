# Задание №1
# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя.
# Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

ids = {
    "user1": [213, 213, 213, 15, 213],
    "user2": [54, 54, 119, 119, 119],
    "user3": [213, 98, 98, 35],
}

empty_set = set()

for key, value in ids.items():
    print(key, value)
    empty_set.update(value)

print(f"Результат: {empty_set}")


# Задание №2
# Дана переменная, в которой хранится список поисковых запросов пользователя.
# Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.

queries = [
    "смотреть сериалы онлайн",
    "новости спорта",
    "афиша кино",
    "курс доллара",
    "сериалы этим летом",
    "курс по питону",
    "сериалы про спорт",
    "это будет тестовое предложение",
]

empty_list = list()

for query in queries:
    count_word = len(query.split())
    empty_list.append(count_word)

for item in set(empty_list):
    print(
        f"Поисковых запросов, содержащих {item} слов(а): {round(empty_list.count(item) / len(empty_list) * 100, 2)}%"
    )


# Задание №3
# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам.
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100.

results = {
    "vk": {"revenue": 103, "cost": 98},
    "yandex": {"revenue": 179, "cost": 153},
    "facebook": {"revenue": 103, "cost": 110},
    "adwords": {"revenue": 35, "cost": 34},
    "twitter": {"revenue": 11, "cost": 24},
}

for key in list(results.keys()):
    results[key]["ROI"] = round(
        (results[key]["revenue"] / results[key]["cost"] - 1) * 100, 2
    )


# Задание №4
# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж.
# Напишите программу, которая возвращает название канала с максимальным объемом продаж.

stats = {
    "facebook": 55,
    "yandex": 115,
    "vk": 120,
    "google": 99,
    "email": 42,
    "ok": 98,
    "netology": 120,
}

max_keys = [key for key, value in stats.items() if value == max(stats.values())]

print(f"Больше всего продаж в компаниях: {', '.join(max_keys)}")


# Задание №5
# Дан список произвольной длины.
# Написать код, который на основе исходного списка составит словарь такого уровня вложенности, какова длина исходного списка.

my_list = ["a", "b", "c", "d", "e", "f"]

empty_dict = my_list[-1]

for item in reversed(my_list[:-1]):
    empty_dict = {item: empty_dict}

print(empty_dict)


# Задание №6
# Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления блюда в расчете на одну порцию.
# Напишите программу, которая будет запрашивать у пользователя количество порций для приготовления этих блюд и отображать информацию о суммарном количестве требуемых ингредиентов в указанном виде.
# Внимание! Одинаковые ингредиенты с разными размерностями нужно считать раздельно!

cook_book = {
    "салат": [
        {"ingridient_name": "сыр", "quantity": 50, "measure": "гр"},
        {"ingridient_name": "томаты", "quantity": 2, "measure": "шт"},
        {"ingridient_name": "огурцы", "quantity": 20, "measure": "гр"},
        {"ingridient_name": "маслины", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "оливковое масло", "quantity": 20, "measure": "мл"},
        {"ingridient_name": "салат", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "перец", "quantity": 20, "measure": "гр"},
    ],
    "пицца": [
        {"ingridient_name": "сыр", "quantity": 20, "measure": "гр"},
        {"ingridient_name": "колбаса", "quantity": 30, "measure": "гр"},
        {"ingridient_name": "бекон", "quantity": 30, "measure": "гр"},
        {"ingridient_name": "оливки", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "томаты", "quantity": 20, "measure": "гр"},
        {"ingridient_name": "тесто", "quantity": 100, "measure": "гр"},
    ],
    "лимонад": [
        {"ingridient_name": "лимон", "quantity": 1, "measure": "шт"},
        {"ingridient_name": "вода", "quantity": 200, "measure": "мл"},
        {"ingridient_name": "сахар", "quantity": 10, "measure": "гр"},
        {"ingridient_name": "лайм", "quantity": 20, "measure": "гр"},
    ],
}

user_input = int(input("Введите количество порций: "))

empty_dict = {}

for recipe in cook_book.values():
    for detail in recipe:
        name = detail["ingridient_name"]
        user_quantity = detail["quantity"] * user_input
        measure = detail["measure"]

        if name not in empty_dict:
            empty_dict[name] = {"quantity": user_quantity, "measure": measure}
        else:
            empty_dict[name]["quantity"] += user_quantity

for name, count in empty_dict.items():
    print(f"{name}: {count['quantity']} {count['measure']}")

