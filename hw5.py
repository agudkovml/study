import json
import csv

# Задание №1
# Переведите содержимое файла purchase_log.txt* в словарь purchases вида:
# - {‘1840e0b9d4’: ‘Продукты’, …}

purchases = dict()

with open("purchase_log.txt", "r") as pl:
    for i, line in enumerate(pl):
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        if i == 0 and obj["user_id"] == "user_id":
            continue
        purchases[obj["user_id"]] = obj["category"]


# Задание №2
# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки, если покупка была, сам файл visit_log.csv* изменять не надо. 
# Запишите в файл funnel.csv визиты из файла visit_log.csv*, в которых были покупки с указанием категории.
# Учтите условия на данные:
# - содержимое purchase_log.txt* помещается в оперативную память компьютера;
# - содержимое visit_log.csv* — нет; используйте только построчную обработку этого файла.

with(
    open("visit_log.csv", "r") as vlread,
    open("funnel.csv", "w") as fwrite
):
    reader = csv.reader(vlread)
    writer = csv.writer(fwrite)
    
    for row in reader:
        user_id = row[0]
        category = purchases.get(user_id)
        if category:
            writer.writerow(row + [category])    
        
        
        