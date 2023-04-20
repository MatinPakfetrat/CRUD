"""This module implements the user interactivity."""

from ResourceManager import ResourceManager
from DataPersistence import DataPersistence

class UserInteractivity:

    def __init__(self):
        self.ResourceManager = ResourceManager()
        self.DataPersistence = DataPersistence()
    
    def display_menu(self):
        """Displays the menu of options."""
        print("\nMenu:")
        print("1. Create book")
        print("2. Search books")
        print("3. Edit book")
        print("4. Delete book")
        print("5. Exit")
        return input("Please choose an option: ")
    
    def run(self):
        """Runs the program."""
        self.DataPersistence.load_data(self.ResourceManager)
        if self.ResourceManager.resources:
            print("\nBook(s): ")
            for resource in self.ResourceManager.resources:
                resource.display()

        while True:
            choice = self.display_menu()
            if choice == "1":
                while True:    
                    try:
                        id = int(input("Please enter the ID of the book: "))
                        name = input("Please enter the name of the book: ").capitalize()
                        author = input("Please enter the name of the author of the book: ").capitalize()
                        date = int(input("Please enter the publication year of the book: "))
                        if self.ResourceManager.create_resource(id, name, author, date):
                            print("Book created successfully!")
                            break
                    except ValueError:
                        print("Invalid input! Try again.")    
            elif choice == "2":
                while True:
                    try:
                        id = int(input("Please enter the ID of the book: "))
                        name = input("Please enter the name of the book: ").capitalize()    
                        print()
                        self.ResourceManager.search_resource(id, name)
                        break
                    except ValueError:
                        print("Invalid input! Try again.")    
            elif choice == "3":
                while True:
                    try:
                        id = int(input("Please enter the ID of the book: "))
                        self.ResourceManager.edit_resource(id)
                        break
                    except ValueError:
                        print("Invalid input! Try again.")    
            elif choice == "4":
                while True:
                    try:
                        id = int(input("Please enter the ID of the book: "))            
                        self.ResourceManager.delete_resource(id)
                        break
                    except ValueError:
                        print("Invalid input! Try again.")   
            elif choice == "5":
                # Saves the resource data to the file before exiting the program
                self.DataPersistence.save_data(self.ResourceManager)
                break
            else:
                print("Invalid choice. Please try again.")

ui = UserInteractivity()
ui.run()
