import os

def insert_grade():
    book = {}

    while True:
        code = int(input('enter code: '))
        title = input('enter book name: ')
        if code == -1:
            break
        if code not in book.keys():
            book[code] = title

    return book
        

