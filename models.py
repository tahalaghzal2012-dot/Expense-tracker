import json
from storage import StorageManager


class ExpenseTracker():
    def __init__(self):
        self.amount = int(input("Insert expense amount: "))
        self.description = input("Insert a description if avaiable or leave it empty: ")
        self.category = input("Insert a category name (creat one or add to existing one): ")
    
    def ai_list_creator():
        st_ai_reply = StorageManager(None, "data.json")
        data = st_ai_reply.loading()
        clist = json.dumps(data, indent=4)
        return clist