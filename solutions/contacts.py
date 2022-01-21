#!/usr/bin/env python
import argparse
import pprint
import re

"""
Our data structure allowing to store e-mail addresses associated to names
"""
contacts = {
    "pro": {
        "Maria": "maria.d@business.fr",
        "Jérôme": "j@gmail.com",
    },
    "perso": {
        "Maria": "maria@dupont.fr",
        "Jérôme": "j@gmail.com",
        "Joseph": "joseph@free.fr",
    },
}



def add(contacts, book, name, email):
    """
    Function adding a new entry (name + e-mail) to the contacts data structure, with side effect
    """
    if email is None:
        raise ValueError("-email argument is needed")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("{} isn't a valid email format".format(email))
    contacts[book][name] = email


def delete(contacts, book, name):
    """
    Function searching an entry based on its e-mail and deleting it if found, with side effect
    """
    if name not in contacts[book]:
        print(contacts[book])
        raise KeyError("{} contact not found in book {}".format(name, book))
    del contacts[book][name]


def search(contacts, book, name):
    """
    Function searching an entry based on its e-mail and printing it if found
    """
    books = [book] if not book else ["pro", "perso"]
    for book in books:
        if name in contacts[book]:
            print("Book {} has email {} for {}".format(book, contacts[book][name], name))


parser = argparse.ArgumentParser()
parser.add_argument("command", type=str, choices=["add", "del", "search"])
parser.add_argument("name", type=str)
parser.add_argument("-email", type=str)
parser.add_argument("-b", "--book", type=str, default="perso", choices=["pro", "perso"])


args = parser.parse_args()
if args.command == "add":
    add(contacts, args.book, args.name, args.email)
elif args.command == "del":
    delete(contacts, args.book, args.name)
elif args.command == "search":
    search(contacts, args.book, args.name)


pprint.PrettyPrinter(indent=4).pprint(contacts)
