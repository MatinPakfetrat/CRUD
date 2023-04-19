"""This module creates and manipulates instances of the resource class."""

from Resource import Resource

class ResourceManager:
    
    def __init__(self):
        self.resources = [Resource(1, "ahsdgi", "agolsjfd", 310635)]

    def create_resource(self, id, name, author, date):
        for resource in self.resources:
            if resource.id == id:
                print("A resource with this ID already exists! Try again.")
                return
        self.resources.append(Resource(id, name, author, date))
        print("Resource created successfully!")
    
    def search_resource(self, id, name):
        found = []
        for resource in self.resources:
            if resource.id == id and resource.name == name:
                found.append(resource)
        if found:
            print("Found resource(s):")  
            for r in found:
                r.display()    
        else:
            print("No resources found! Try again.")

    def edit_resource(self, id):
        for i in range(0, len(self.resources)):
            if self.resources[i].id == id:
                while True:
                    try:            
                        new_name = input("Please enter the updated name of the resource: ")
                        new_author = input("Please enter the updated name of the author of the resource: ")
                        new_date = int(input("Please enter the updated publication year of the resource: "))
                        break
                    except ValueError:
                        print("Invalid input! Try again.")
                self.resources[i] = Resource(id, new_name, new_author, new_date)
                return "Resource information updated successfully!"        
        print("No resources found! Try again.")    

    def delete_resource(self, id):
        for i in range(0, len(self.resources)):
            if self.resources[i].id == id:
                del(self.resources[i])
                print("Resource deleted successfully!")
                return
        print("No resources found!")        
