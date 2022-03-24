import json
import csv

name_file_csv = 'books.csv'
name_file_json = "users.json"


def manipulation_books():
    list_book = []
    with open(name_file_csv) as File:
        reader = csv.DictReader(File)
        for row in reader:
            list_book.append(row)
    for i in range(len(list_book)):
        dictionary = list_book[i]
        dictionary['title'] = dictionary.pop('Title')
        dictionary['author'] = dictionary.pop('Author')
        dictionary['pages'] = dictionary.pop('Pages')
        dictionary['genre'] = dictionary.pop('Genre')
        dictionary.pop('Publisher')
    return list_book


def manipulation_user():
    list_user = []
    with open(name_file_json, "r") as read_file:
        data = json.load(read_file)
    for i in range(len(data)):
        example = {
                "name": f"{data[i]['name']}",
                "gender": f"{data[i]['gender']}",
                "address": f"{data[i]['address']}",
                "age": data[i]['age'],
                "books": []}
        list_user.append(example)
    return list_user


def distribution_book():
    list_user = manipulation_user()
    list_book = manipulation_books()
    while len(list_book) > 0:
        for j in range(len(list_user)):
            for i in range(len(list_book) - 1, -1, -1):
                list_user[j]["books"].append(list_book[i])
                list_book.pop(i)
                break
    return list_user


def create_json_file():
    with open("result.json", "w") as write_file:
        json.dump(distribution_book(), write_file, indent=4)


create_json_file()
