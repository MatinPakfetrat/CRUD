"""This module persists all data into an appropriate text file."""

import csv

class DataPersistence:

    def load_data(self, resource_manager):
        """Loads the data from the text file and creates the resources."""
        try:
            with open("Resources.csv", 'r') as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    resource_manager.create_resource(row[0], row[1], row[2], row[3])
        except FileNotFoundError:
            print("Data file not found. Starting with empty resource manager.")

    def save_data(self, resource_manager):
        """Saves the changes to the resources in the file."""
        try:
            with open("Resources.csv", 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Name", "Author", "Date"])
                for resource in resource_manager.get_all_resources():
                    writer.writerow(resource.get_attributes())
        except IOError:
            print("Error saving data. Changes will not be persisted.")        
            