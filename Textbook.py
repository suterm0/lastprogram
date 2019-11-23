from Person import Person


class Textbook():

    def __init__(self, title, first, last, age, edition, number, publisher, year_published, quantity, price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.number = number
        self.publisher = publisher
        self.year_published = year_published
        self.quantity = quantity
        self.price = price

    def description(self):
        print(f"Here is the text book Details you entered"
              f" Edition: {self.edition} "
              f" ISBN Number: {self.number} "
              f" Publisher: {self.publisher} "
              f" Year Published: {self.year_published} "
              f" Inventory left: {self.quantity} "
              f" Price: ${self.price} ")

    def add_inventory(self, qty):
        self.quantity = self.quantity + qty

    def remove_inventory(self, qty):
        self.quantity = self.quantity - qty

