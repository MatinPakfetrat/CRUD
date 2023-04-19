"""This module implements the user interactivity."""

from ResourceManager import ResourceManager
from DataPersistence import DataPersistence

class UserInteractivity:
    
    def display_menu(self):

        print("\nMenu:")
        print("1. Create resource")
        print("2. Read resource")
        print("3. Edit resource")
        print("4. Delete resource")
        print("5. Exit")
        return input("Please choose an option: ")
    
    def run(self):

        while True:
            choice = self.display_menu()
            if choice == "1":
                ResourceManager.create_resource()
            elif choice == "2":
                ResourceManager.read_resource()
            elif choice == "3":
                ResourceManager.edit_resource()
            elif choice == "4":
                ResourceManager.delete_resource()
            elif choice == "5":
                # Save the resource data to the file before exiting the program
                DataPersistence.save_data()
                break
            else:
                print("Invalid choice. Please try again.")
                