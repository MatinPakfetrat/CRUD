"""This module creates and manipulates instances of the resource class."""

from Resource import Resource

class ResourceManager:

    def __init__(self):
        self.resources = []

    def create_resource(self, id, name, author, date):
        """Creates a book."""
        for resource in self.resources:
            if int(resource.get_id()) == id:
                print("A book with this ID already exists! Try again.")
                return
        self.resources.append(Resource(id, name, author, date))
        return True
    
    def search_resource(self, id, name):
        """Searches for a book."""
        flag = False
        for resource in self.resources:
            if int(resource.get_id()) == id and str(resource.get_name()) == name:
                flag = True
                break
        if flag:        
            print("Found book:", end=' ')
            resource.display()     
        else:
            print("No book found!")

    def edit_resource(self, id):
        """Edits a book if found."""
        for i in range(0, len(self.resources)):
            if int(self.resources[i].get_id()) == id:
                while True:
                    try:            
                        new_name = input("Please enter the updated name of the book: ").capitalize()
                        new_author = input("Please enter the updated name of the author of the book: ").capitalize()
                        new_date = int(input("Please enter the updated publication year of the book: "))
                        break
                    except ValueError:
                        print("Invalid input! Try again.")
                self.resources[i] = Resource(id, new_name, new_author, new_date)
                print("Book's information updated successfully!")
                return        
        print("No book found! Try again.")    

    def delete_resource(self, id):
        """Deletes a book if found."""
        for i in range(0, len(self.resources)):
            if int(self.resources[i].get_id()) == id:
                del(self.resources[i])
                print("Book deleted successfully!")
                return
        print("No book found!")        

    def get_all_resources(self):
        return self.resources
    