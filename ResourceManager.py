"""This module creates and manipulates instances of the resource class."""

from Resource import Resource

class ResourceManager:
    
    def __init__(self):
        self.resources = []

    def create_resource(self, id, name, author, date):
        self.resources.append(Resource(id, name, author, date))
        return "Resource created successfully!"
    