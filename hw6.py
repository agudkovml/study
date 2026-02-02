from datetime import datetime, timedelta

# Задание №1
# Печатные газеты использовали свой формат дат для каждого выпуска.
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:

moscow_times = "Wednesday, October 2, 2002"
the_guardian = "Friday, 11.10.13"
daily_news = "Thursday, 18 August 1977"

mt_format = datetime.strptime(moscow_times, "%A, %B %d, %Y")
tg_format = datetime.strptime(the_guardian, "%A, %d.%m.%y")
dn_format = datetime.strptime(daily_news, "%A, %d %B %Y")


# Задание 2
# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения
# Напишите функцию, которая проверяет эти даты на корректность. То есть для каждой даты возвращает True — дата корректна или False — некорректная.

stream = ["2018-04-02", "2018-02-29", "2018-19-02"]

def date_validate(date_list: list[str]) -> bool:
    stream_bool = []    # Можно сделать и через dict, где key это stream[i], а value bool
    
    for date in date_list:
        try:
            if datetime.strptime(date, "%Y-%m-%d"):
                stream_bool.append(True)
        except ValueError:
            stream_bool.append(False)

    return stream_bool

# Задание №3
# Напишите функцию date_range, которая возвращает список дат за период от start_date до end_date.
# Даты должны вводиться в формате YYYY-MM-DD.
# В случае неверного формата или при start_date > end_date должен возвращаться пустой список.


def date_range() -> list[datetime]:
    try:
        start_date = datetime.strptime(input(), "%Y-%m-%d")
        end_date = datetime.strptime(input(), "%Y-%m-%d")
        if start_date > end_date:
            return []
    except ValueError:
        return []

    return [
        datetime.strftime(start_date + timedelta(days=i), "%Y-%m-%d")
        for i in range((end_date - start_date).days + 1)
    ]


# Задание №4
# -Что значит ошибка list index out of range?
# -Почему при первом запуске функция работает корректно, а при втором — нет?


DEFAULT_USER_COUNT = 3


def delete_and_return_last_user(region, default_list=["A100", "A101", "A102"]):
    """
    Удаляет из списка default_list последнего пользователя
    и возвращает ID нового последнего пользователя.
    """

    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)

    return default_list[DEFAULT_USER_COUNT - 2]


print(delete_and_return_last_user(1), delete_and_return_last_user(1))
# 1. List index out of range возникает именно потому, что список «запомнил» изменения от первого вызова и стал короче.
# 2. При повторном запуске функция не отрабатывает потому что была нарушена одна из критических ошибок, в которой говорится, что объекты не стоит(иногда нельзя) изменять во итерации.
#    Потому что индексы при удалении смещаются, а на 0-ой итерации все индексы на месте(переменные сделаны под начальное состояние функции), по этому она правильно отрабатывает
