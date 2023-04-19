"""This module defines the properties of the resources."""

class Resource:

    def __init__(self, id, name, author, date):
        self.id = id
        self.name = name
        self.author = author
        self.date = date

    def display(self):
        print(f"ID: {self.id}, name: {self.name}, author: {self.author}, date: {self.date}")

    def get_attributes(self):
        return [self.id, self.name, self.author, self.date]
