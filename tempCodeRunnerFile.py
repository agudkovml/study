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
