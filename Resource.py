"""This module defines the properties of the resources."""

class Resource:

    def __init__(self, id, name, author, date):
        self.id = id
        self.name = name
        self.author = author
        self.date = date

    def display(self):
        """Displays the attributes of the book."""
        print(f"ID: {self.id}, Name: {self.name}, Author: {self.author}, Date: {self.date}")

    def get_attributes(self):
        return [self.id, self.name, self.author, self.date]
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
