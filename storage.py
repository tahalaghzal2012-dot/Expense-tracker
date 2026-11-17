import json
from datetime import datetime
current_time = datetime.now()

class StorageManager:
    def __init__(self, data, filename):
        self.data = data
        self.empty_list = []
        self.filename = filename
        self.now = current_time.strftime("%Y-%m-%d %H:%M:%S")
    def loading(self):
        try:
            with open(self.filename, "r") as file:
                loaded_data = json.load(file)
                return loaded_data
            
        except FileNotFoundError:
            return self.empty_list
        
        except json.JSONDecodeError:
            print("Data is currupted!")
            return self.empty_list
        
        except PermissionError:
            print("File not accesible!")
            print("Please try again later!")
            quit()

    def saving(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    
