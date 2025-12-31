#Задание №1
#Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:
#-среднюю букву, если число букв в слове нечетное;
#-две средних буквы, если число букв четное.

input_user = "word"
input_quantity = len(input_user)

if input_quantity % 2 == 0:
    i = int(input_quantity / 2)
    print(f"{input_user[i - 1]}{input_user[i]}")
else:
    i = int(input_quantity / 2)
    print(input_user[i])
    
    
#Задание №2
#Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз).
#После первого нуля выводит сумму всех ранее введенных чисел.

list_user = []

list_user.append(int(input("Введите число: ")))

while list_user[-1] != 0:
    list_user.append(int(input("Введите число: ")))

print(f"Результат: {sum(list_user)}")


#Задание №3
#Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
#Выдвигаем гипотезу: 
#-лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки!
#-но мы не будем никого знакомить, если кто-то может остаться без пары

boys = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha", "Valya"]
boys.sort()
girls.sort()

if len(boys) == len(girls):
    for i, j in zip(boys, girls):
        print(i, j)
else:
    print("Кто-то может остаться без пары!")
    
    
#Задание №4
#У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам. 
#Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях для каждой страны.

countries_temperature = [
["Таиланд", [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
["Германия", [57.2, 55.4, 59, 59, 53.6]],
["Россия", [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
["Польша", [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print("Результаты: ")
for i in countries_temperature:
    temperature_average = sum(i[1]) / len(i[1])
    temperature_celsius = round((temperature_average - 32) * 5 / 9, 1)
    print(i[0], temperature_celsius)
    
    
#Задание №5
#Имеется список с транспортными номерами. 
#Необходимо написать код, который проверит каждый номер на валидность (1 буква, 3 цифры, 2 буквы, 2-3 цифры). 
#Обратите внимание, что не все буквы кириллического алфавита используются в транспортных номерах.

import re

car_ids = ["А222ВС96", "АБ22ВВ193", "К228ВО62"]
pattern = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"

for license_plate in car_ids:
    if re.search(pattern, license_plate):
        pattern_number = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}"
        pattern_region = r"\d{2,3}"
        number = re.search(pattern_number, license_plate).group()
        region = re.search(pattern_region, license_plate[5:]).group()
        print(f"Номер {number} валиден. Регион {region}")
    else:
        print(f"{license_plate} Не валиден")
    
    
#Задание №6
#Дан поток логов по количеству просмотренных страниц для каждого пользователя (пользователь,дата;просмотры).
#Вам необходимо написать алгоритм, который считает среднее значение просмотров на пользователя.

stream = [             
"user4,2021-01-01;3",
"user3,2022-01-07;4",  
"user2,2022-03-29;1",
"user1,2020-04-04;13",
"user2,2022-01-05;7",
"user1,2021-06-14;4",
"user3,2022-07-02;10",
"user4,2021-03-21;19",
"user4,2022-03-22;4",
"user4,2022-04-22;8",
"user4,2021-05-03;9",
"user4,2022-05-11;11"
]

import re

user_dict = {}

pattern = r"^([^,]+),(.*);([^;]+)$"

for log in stream:
    before_comma = re.search(pattern, log).group(1)
    after_semicolon = int(re.search(pattern, log).group(3))
    if before_comma in user_dict:
        user_dict[before_comma] += after_semicolon
    else:
        user_dict[before_comma] = after_semicolon
        
unique_sum_value = 0        

for user in user_dict.values():
    unique_sum_value += user
    
print(unique_sum_value / len(user_dict))
