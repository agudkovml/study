# Код должен быть грамотно декомпозирован (каждая функция отвечает за свою конкретную задачу, дублирующийся функционал переиспользуется, а его код не повторяется);
# -коде отсутствуют глобальные переменные (за исключением books и directories);
# -пользовательский ввод обрабатывается в цикле while до тех пор, пока пользователь явно не завершит программу (вводом команды “q”);
# -код обязательно должен содержать конструкцию match case и метод словаря setdefault().\

# Перечень всех книг в библиотеке
books = [
    {
        "genre": "поэзия",
        "number": "978-5-1000-1234-7",
        "title": "Евгений Онегин",
        "author": "Александр Пушкин",
    },
    {
        "genre": "фэнтези",
        "number": "88006",
        "title": "Властелин колец",
        "author": "Джон Р. Р. Толкин",
    },
    {
        "genre": "детектив",
        "number": "D-1122",
        "title": "Безмолвный свидетель",
        "author": "Агата Кристи",
    },
]


# Перечень полок, на которых хранятся книги
directories = {"1": ["88006"], "2": ["D-1122"], "3": []}


# Задание №1
# Пункт №1. Пользователь по команде “book_info” может найти название книги и её автора


def book_info(number_book) -> str | int:
    for book in books:
        if book["number"] == number_book:
            return book["number"], book["author"], book["title"], book["genre"]

    return 0


# Пункт №2. Пользователь по команде “shelf” может по названию книги узнать, на какой полке она хранится


def shelf(name_book) -> str | int:
    for book in books:
        if name_book == book["title"]:
            for key, value in directories.items():
                if book["number"] in value:
                    return key

    return 0


# Пункт №3. Пользователь по команде “all” может увидеть полную информацию по всем книгам


def all() -> str:
    for book in books:
        shelf_book = shelf(book["title"])
        if shelf_book == 0:
            shelf_book = None
        print(
            f"№: {book['number']}, жанр: {book['genre']}, название: {book['title']}, автор: {book['author']}, полка хранения: {shelf_book}"
        )


# Пункт 4. Пользователь по команде “add_shelf” может добавить новую полку


def add_shelf():
    shelf_number = input("Введите номер полки: ")
    if shelf_number in directories.keys():
        print(
            f"Такая полка уже существует. Текущий перечень полок: {', '.join(directories.keys())}"
        )
    else:
        directories.setdefault(shelf_number, [])
        print(
            f"Полка добавлена. Текущий перечень полок: {', '.join(directories.keys())}"
        )


# Пункт №5. Пользователь по команде “del_shelf” может удалить существующую полку из данных (только если она пустая)


def del_shelf() -> str:
    shelf_number = input("Введите номер полки: ")

    if shelf_number not in directories.keys():
        print(
            f"Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}"
        )
    elif not directories.get(shelf_number):
        directories.pop(shelf_number)
        print(f"Полка удалена. Текущий перечень полок: {', '.join(directories.keys())}")
    else:
        print(
            f"На полке есть книги, удалите их перед использованием. Текущий перечень полок: {', '.join(directories.keys())}"
        )


# Задание №2
# Пункт №1. Пользователь по команде “add_book” может добавить новую книгу в данные


def add_book(number, genre, title, author, shelf) -> int:
    if shelf in directories.keys():
        new_books = {"genre": genre, "number": number, "title": title, "author": author}
        books.append(new_books)
        directories.setdefault(shelf, []).append(number)
        return 1
    else:
        return 0


# Пункт №2. Пользователь по команде “del_book” может удалить книгу из данных


def del_book(number) -> int | str:
    for index, book in enumerate(books):
        if number == book["number"]:
            books.pop(index)
            print("Книга удалена.\nТекущий список книг:")
            all()
            return 1

    print("Книга не найдена в базе.\nТекущий список книг:")
    all()


# Пункт №3. Пользователь по команде “move” может переместить книгу с полки на полку


def move() -> None:
    number_book = input("Введите номер книги: ")

    if not any(book["number"] == number_book for book in books):
        print("Книга не найдена в базе.\nТекущий список книг:")
        all()
        return

    current_shelf = None
    for shelf_key, book_numbers in directories.items():
        if number_book in book_numbers:
            current_shelf = shelf_key
            break

    if current_shelf is None:
        print("Книга есть в базе, но не привязана ни к одной полке")
        return

    new_shelf = input("Введите номер полки: ")

    if new_shelf not in directories:
        print(
            f"Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}"
        )
        return

    directories[current_shelf].remove(number_book)
    directories.setdefault(new_shelf, []).append(number_book)

    print("Книга перемещена.\nТекущий список документов:")
    all()


def main():
    user_input = 0
    while user_input != "q":
        user_input = input("Введите команду: ")
        match user_input:
            case "book_info":
                number_book = input("Введите номер книги: ")
                book_data = book_info(number_book)
                if book_data != 0:
                    print(f"Название книги: {book_data[2]}\nАвтор: {book_data[1]}")
                else:
                    print("Книга не найдена")
            case "shelf":
                name_book = input("Введите название книги: ")
                key = shelf(name_book)
                if key != 0:
                    print(f"Книга хранится на полке: {key}")
                else:
                    print("Книга не найдена в базе")
            case "all":
                all()
            case "add_shelf":
                add_shelf()
            case "del_shelf":
                del_shelf()
            case "add_book":
                number = input("Введите номер книги: ")
                genre = input("Введите жанр книги: ")
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                shelf = input("Введите полку для хранения: ")
                result = add_book(number, genre, title, author, shelf)
                if result == 1:
                    print("Книга добавлена. Текущий список книг:")
                    all()
                else:
                    print(
                        "Такой полки не существует. Добавьте полку командой add_shelf.\nТекущий список книг:"
                    )
                    all()

            case "del_book":
                number = input("Введите номер книги: ")
                del_book(number)
            case "move":
                move()


if __name__ == "__main__":
    main()