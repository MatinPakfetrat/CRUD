"""This module implements the user interactivity."""

from ResourceManager import ResourceManager
from DataPersistence import DataPersistence

class UserInteractivity:

    ResourceManager = ResourceManager()
    DataPersistence = DataPersistence()
    
    def display_menu(self):

        print("\nMenu:")
        print("1. Create resource")
        print("2. Search resources")
        print("3. Edit resource")
        print("4. Delete resource")
        print("5. Exit")
        return input("Please choose an option: ")
    
    def run(self):

        while True:
            choice = self.display_menu()
            if choice == "1":
                while True:    
                    try:
                        id = int(input("Please enter the ID of the resource: "))
                        name = input("Please enter the name of the resource: ")
                        author = input("Please enter the name of the author of the resource: ")
                        date = int(input("Please enter the publication year of the resource: "))
                        self.ResourceManager.create_resource(id, name, author, date)
                        break
                    except ValueError:
                        print("Invalid input! Try again.")    
            elif choice == "2":
                while True:
                    try:
                        id = int(input("Please enter the ID of the resource: "))
                        name = input("Please enter the name of the resource: ")    
                        self.ResourceManager.search_resource(id, name)
                        break
                    except ValueError:
                        print("Invalid input! Try again.")    
            elif choice == "3":
                while True:
                    try:
                        id = int(input("Please enter the ID of the resource: "))
                        print(self.ResourceManager.edit_resource(id))
                        break
                    except ValueError:
                        print("Invalid input! Try again.")    
            elif choice == "4":
                self.ResourceManager.delete_resource()
            elif choice == "5":
                # Save the resource data to the file before exiting the program
                self.DataPersistence.save_data()
                break
            else:
                print("Invalid choice. Please try again.")
u = UserInteractivity()
u.run()