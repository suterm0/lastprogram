#Michael Suter
#
#11.20.19

from Person import Person
from Textbook import Textbook
titles = []
title = input("What is the title of the book?>>")
titles.append(title)
first = input("Enter the authors first name.>>")
last = input("Enter the authors last name.>>")
age = input("Enter the authors age.>>")
person = (first, last)
author = (first, last, age)
edition = input("Enter the Edition of the book.>>")
number = input("Enter the book number.>>")
publisher = input("Enter the publisher.>>")
year_published = input("Enter the year the book was published.>>")
quantity = input("How many books are there to buy?>>")
price = input("How much does the book cost?>>")
first_book = Textbook(title, first, last, age, author, edition, number, publisher, year_published, quantity, price)


def menu():
    h = 2
    while h == 2:
        answer = input("Would you like to add a book to the library?(Y/N).>>")
        if answer == 'y' and 'Y':
            print(f"Here is your first books details:"
                  f"{first_book}.")
        elif answer == 'n' and 'N':
            exit("Thanks. Goodbye.")
        else:
            print("Invalid response. Please answer with (Y/N).")


Textbook.description()
menu()
