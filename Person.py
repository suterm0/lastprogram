#Michael Suter
#
#11.20.19


class Person():

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def personal_description(self):
        print(f"This Persons name is {self.first} {self.last} and they are {self.age} years old")
