"""This module creates and manipulates instances of the resource class."""

from Resource import Resource

class ResourceManager:
    
    def __init__(self):
        self.resources = []

    def create_resource(self, id, name, author, date):
        self.resources.append(Resource(id, name, author, date))
        return "Resource created successfully!"
    
    def search_resource(self, id, name):
        found = []
        for resource in self.resources:
            if resource.id == id and resource.name == name:
                found.append(resource)
        if found:
            return "Found resource(s):", print(r for r in found)         
        else:
            return "No resources found."
    