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
person = Person.personal_description
author = (first, last, age)
edition = input("Enter the Edition of the book.>>")
number = input("Enter the book ISBN number.>>")
publisher = input("Enter the publisher.>>")
year_published = input("Enter the year the book was published.>>")
quantity = int(input("How many books are there to buy?>>"))
price = int(input("How much does the book cost?>>"))
first_book = Textbook(title, first, last, age, edition, number, publisher, year_published, quantity, price)


def menu():
    print(f"You have successfully added {title} to the library. ")
    print(f"Here is a current list of books in the library{titles}")
    answer = input("Would you like to add a book to the library?(Y/N).>>")
    if answer == 'y' and 'Y':
        title2 = input("What is the title of the book?>>")
        titles.append(title2)
        first2 = input("Enter the authors first name.>>")
        last2 = input("Enter the authors last name.>>")
        age2 = input("Enter the authors age.>>")
        person2 = Person.personal_description
        author2 = (first2, last2, age2)
        edition2 = input("Enter the Edition of the book.>>")
        number2 = input("Enter the book number.>>")
        publisher2 = input("Enter the publisher.>>")
        year_published2 = input("Enter the year the book was published.>>")
        quantity2 = int(input("How many books are there to buy?>>"))
        price2 = int(input("How much does the book cost?>>"))
        total = quantity + quantity2
        second_book = Textbook(title2, first2, last2, age2, edition2, number2, publisher2, year_published2, quantity2, price2)
        print(f"There are now two different books in stock, There is {quantity} {title}'s and there is {quantity2} of {title2}.")
        print(f"There is a total of {total} books in inventory right now")
    elif answer == 'n' and 'N':
        exit("Thanks. Goodbye.")
    else:
        print("Invalid response. Please answer with (Y/N).")
    play_again = 2
    while play_again == 2:
        answer2 = input("Would you like to add a book to the library?(Y/N).>>")
        if answer2 == 'y' and 'Y':
            title3 = input("What is the title of the book?>>")
        titles.append(title3)
        first2 = input("Enter the authors first name.>>")
        last2 = input("Enter the authors last name.>>")
        age2 = input("Enter the authors age.>>")
        person2 = Person.personal_description
        author2 = (first2, last2, age2)
        edition2 = input("Enter the Edition of the book.>>")
        number2 = input("Enter the book number.>>")
        publisher2 = input("Enter the publisher.>>")
        year_published2 = input("Enter the year the book was published.>>")
        quantity2 = int(input("How many books are there to buy?>>"))
        price2 = int(input("How much does the book cost?>>"))
        total = quantity + quantity2
        second_book = Textbook(title3, first2, last2, age2, edition2, number2, publisher2, year_published2, quantity2, price2)
        print(f"There are now two different books in stock, There is {quantity} {title}'s and there is {quantity2} of {title3}.")
        print(f"There is a total of {total} books in inventory right now")


first_book.description()
menu()
