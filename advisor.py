import requests
import json 
from storage import StorageManager
from models import ExpenseTracker

ex = ExpenseTracker

stdataloader = StorageManager(None, "data.json")



class agent():
    def __init__(self):
        self.data = stdataloader.loading()
        self.clist = ex.ai_list_creator()
        self.url = "http://localhost:11434/api/chat"
        self.system_prompt = (
            "You are a ruthless, emotionless expense auditor. "
            "Never greet the user, never apologize, never encourage, and never show empathy. "
            "Treat every non-essential purchase as a financial mistake. "
            "Respond only with cold facts, blunt criticism, and strict corrective actions. "
            "You will receive a JSON list of the user's expenses. "
            "Analyze the exact categories, descriptions, amounts, and timestamps provided. "
            "Format every reply strictly into two sections using short bullet points: "
            "AUDIT: (2-3 blunt bullet points critiquing specific expenses, categories, or timing) "
            "and RECOMMENDATIONS: (2-3 strict corrective actions based directly on the data).\n\n"
            f"Expense Data:\n{json.dumps(self.data, indent=2)}"
        )
        
        self.useri = input(f"Type about what u want to know about finance, type 'exit' to quit: ").lower()
        self.payload = {
            "model": "llama3.2:latest",
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.useri},
                
            ],
            "stream": False
        }

    

    def request(self):
        try:
            
            response = requests.post(
                self.url,
                timeout=70,
               json=self.payload,

            ) 

            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("Somthing went wrong!")
        except requests.RequestException:
            print(requests.RequestException)
            quit()
            