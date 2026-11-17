from rich import print
from rich.console import Console
from rich.panel import Panel
from storage import StorageManager
from models import ExpenseTracker
from advisor import agent
import numpy as np
import time


id = 0

console = Console()

menu = (
    "[bold cyan]1.[/bold cyan] Add Expense\n"
    "[bold cyan]2.[/bold cyan] Search Expense\n"
    "[bold cyan]3.[/bold cyan] Delet Expense\n"
    "[bold cyan]4.[/bold cyan] statistics\n"
    "[bold cyan]5.[/bold cyan] Get Help Using AI\n"
    "[bold red]6.[/bold red] Exit"
)


d = []

sttime = StorageManager(None, "data.json")
def dict_creator():

    amount = et.amount
    description = et.description
    category = et.category
    current_time_and_date = sttime.now
    return {"id": id, "Date and time" : current_time_and_date, "Amount": amount, "Description": description, "Category": category}

def search(data):

    it = []
    inp = input("Insert the expense category name: ")

    for item in data:
        if item["Category"].lower() == inp.lower():
            it.append(item)

    for expense in it:
            print(f"id: {expense['id']} | Amount: {expense['Amount']} MAD/DH | Description : {expense['Description']}")

    if not it:
        print("Category not found!")
        time.sleep(1)

def delete_exp(data):

    deletion = []
    inpu = input("Delete expense by category name: ")

    for item in data:
        if item["Category"].lower() == inpu.lower():
            deletion.append(item)

    for item in deletion:
        print(f"id: {item['id']}: | Date and Time: {item['Date and time']} | Amount: {item['Amount']} MAD/DH | Category: {item['Category']}")
    
    dele = int(input("Wich expense you want to delete by id (u can delet one at the time) '0' to exit: "))

    for item in data:
        if item['id'] == dele:
            data.remove(item)
            st3.saving()
            print("Expense deleted succesfully!")
            break

        elif dele == 0:
            break

        else:
            print("ther is no expense with that id!")
            continue


def statistics(data):

    if not data:
        print("No expenses founded!")
        return
    
    amount1 = []
    for am in data:
        amount_np = am["Amount"]
        amount1.append(amount_np)
        amount2 = np.array(amount1)

    return amount2

def statistics_shower(data):
    Total = np.sum(data)
    mean = np.mean(data)
    li = np.min(data)
    maxi = np.max(data)
    return Total, mean, li, maxi



while True:
    
    console.print(
    Panel.fit(
        menu,
        title="[bold green]Welcome to Expense Tracker![/bold green]",
        border_style="bright_blue",
        padding=(1, 4)
    )
    )
    u = input("Insert ur choice: ")

    if u == "1":
        et = ExpenseTracker()
        if et.amount == "":
            print("Amount should be numbers, not alphabets or empty!")
            continue

        else:
            pass
        
        et.category.strip()
        if et.category == "" or et.category.isspace():
            print("U can't leave ctegory empty!")
            continue

        st_u1 = StorageManager(None, "data.json")
        data = st_u1.loading()
        highest_id = 0

        for item in data:
            if item["id"] > highest_id:
                highest_id = item["id"]

        id = highest_id + 1

        dic = dict_creator()
        st = StorageManager(dic, "data.json")
        data.append(dic)
        st.data = data
        st.saving()       
        print("Created Expense Sucesfully!")
        time.sleep(2)

    elif u == "2":
        st1 = StorageManager(None, "data.json")
        data = st1.loading()
        search(data)

    elif u == "3":
        st3 = StorageManager(None, "data.json")
        data = st3.loading()
        delete_exp(data)
        st3.data = data
        st3.saving()

    elif u == "4":
        st4 = StorageManager(None, "data.json")
        data = st4.loading()
        amounts = statistics(data)
        Total, average, minimum, maiximium = statistics_shower(amounts)
        print("-----Summary of your expenses------")
        print("Total amount of spended expense: ", Total)
        print("Average Amount Spended in Expenses: ", average)
        print("Minimum Spended in an expense: ", minimum)
        print("Maximium Spended in an expense: ", maiximium)

    elif u == "5":
        while True:
            ai = agent()
            ai_response = ai.request()
            print(ai_response["message"]["content"])
            if ai.useri == "exit":
                break

    elif u == "6":
        print("Bye Bye!")
        break
        
