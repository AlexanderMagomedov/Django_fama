import sqlite3

PAGE_SIZE = 5
PAGE_BOOK_SIZE = 100


# Функция возвращающая полный список сказок
def give_all_book():
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    book_list_all = (list(map(lambda x: x[0], cursor.execute("SELECT book_name FROM telebot_book").fetchall())))
    connect.close()
    return book_list_all


# Функция, формирующая словарь страниц
def page_list():
    book_list_all = give_all_book()
    book_list_pages = {}
    for i in range(len(book_list_all)//PAGE_SIZE + 1):
        book_list_pages[i] = book_list_all[i*PAGE_SIZE:(i+1)*PAGE_SIZE]
    return book_list_pages


def give_all_book_text(book_name):
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute("SELECT book_text FROM telebot_book WHERE book_name = 'Звездные приключения Фрога.'")
    book_text = cursor.fetchall()
    connect.close()
    return book_text[0][0]


def page_book(book_name):
    book_text = give_all_book_text(book_name).split()
    book_pages = {}
    for i in range(len(book_text)//PAGE_BOOK_SIZE + 1):
        book_pages[i] = ' '.join(book_text[i*PAGE_BOOK_SIZE:(i+1)*PAGE_BOOK_SIZE])
    return book_pages
