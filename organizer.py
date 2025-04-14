import json
import datetime
import random
import time

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

print("Welcome to the personal organizer application, which will help you improve the day-to-day life engagements")

def ToDoList():
    filename= "todolist.json"
    todolist = []
    listlength = int(input("Enter the number of tasks you want to perform: "))

    for i in range(listlength):
        print("Todo list menu: ")
        userlist = input("Enter the task: ")
        todolist.append(userlist)
        print("Your task has been added successfully")
        print("The following are the tasks you have added: ")
        for i in todolist:
            print(i)

def ExpenseTracker():
    filename= "expenses.json"
    expenselist = []
    total = 0
    explen = int(input("Enter the number of expenses you want to add:"))
    for i in range(explen):
        print("Expense Tracker Menu: ")
        userinp = input("Enter the name of expense you want to add: ")
        userexp = int(input("Enter the amount for the expense: "))
        expenselist.append({"Expense": userinp, "Amount": userexp})
        print("Your expense has been added successfully")
        total = total + userexp
        print("The following are the expenses you have added:")
        for i in expenselist:
            print(i)
        print("Total: ", total)

def ContactInfo():
    filename= "contacts.json"
    contactlist = []
    listlength = int(input("Enter the number of contacts you want to feed: "))
    for i in range(listlength):
        name = input("Enter the name of the user: ")
        phone = input("Enter the phone number of the user: ")
        pincode = input("Enter the pincode of the user: ")
        contactlist.append({"Name": name, "Phone": phone, "Pincode": pincode})
        print("Your contact has been saved successfully")
    print("The following are the contacts you added: ")
    print(contactlist)

def NoteBook():
    filename= 	"notes.json"
    notelist = []
    listlength = int(input("Enter the number of notes you want to add: "))
    for i in range(listlength):
        note = input("Enter the title of the note: ")
        notecontent = input("Enter the content for the note: ")
        notelist.append({"Title": note, "Content": notecontent})
        print("Your note has been successfully saved")
        print("The following are the notes you saved: ")
        print(notelist)

        rmv = input("Enter the title of the note you want to remove: ")
        for note in notelist:
            if note["Title"] == rmv:
                notelist.remove(note)
                print("Note removed.")
                break
        else:
            print("Your note is not in the list.")

def UtilitiesA():
    filename= "utilities.json"
    print("Welcome to the utilities menu")
    print("1. Age Calculator")
    print("2. Birthday Countdown")
    print("3. Password Generator")
    print("4. Typing Speed Calculator")
    print("5. Exit")
    choose = int(input("Enter your choice: "))

    if choose == 1:
        print("Welcome to the Age Calculator")
        userdate = int(input("Enter birth date: "))
        usermonth = int(input("Enter birth month: "))
        useryear = int(input("Enter birth year: "))
        today = datetime.date.today()
        thisyear = today.year
        age = thisyear - useryear
        print("Your age is:", age, "years")

    elif choose == 2:
        print("Welcome to the Birthday Countdown")
        userdate = int(input("Enter birth date: "))
        usermonth = int(input("Enter birth month: "))
        useryear = int(input("Enter birth year: "))
        today = datetime.date.today()
        birthday = datetime.date(today.year, usermonth, userdate)
        if birthday < today:
            birthday = datetime.date(today.year + 1, usermonth, userdate)
        daysleft = birthday - today
        print("Your birthday is in:", daysleft.days, "days")

    elif choose == 3:
        print("Welcome to the Password Generator")
        lenpass = int(input("Enter the length of the password: "))
        small = "abcdefghijklmnopqrstuvwxyz"
        capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
        symbols = "!@#$%^&*()_+{,}:"
        mix = small + capital + num + symbols
        password = ""
        for i in range(lenpass):
            password += random.choice(mix)
        print("Your password is:", password)

    elif choose == 4:
        print("Welcome to the Typing Speed Calculator")
        sentence = "To commence this undertaking, it is imperative to ensure that Python is firmly ensconced."
        print("Type this sentence within 30 seconds:")
        print(sentence)
        starttime = time.time()
        userinput = input("Type the sentence: ")
        endtime = time.time()
        time_taken = endtime - starttime
        timelimit = 30
        print("You typed the sentence in:", round(time_taken,2), "seconds")
        time_in_minutes = time_taken / 60
        words_typed = len(userinput.split())
        wpm = words_typed / time_in_minutes
        print(f"Your typing speed is approximately {wpm:.2f} WPM.")
        if time_taken > timelimit:
            print("Time is up!")
        else:
           print("you completed within time limit")

    elif choose == 5:
        print("Exiting the utilities menu.")

    else:
        print("Invalid choice in utilities.")


while True:
    print("\nMain Menu:")
    print("1. To-Do List")
    print("2. Expense Tracker")
    print("3. Contact Book")
    print("4. Notes")
    print("5. Utilities")
    print("6. Exit")

    choice = input("Choose an option (1–6): ")

    if choice == "1":
        ToDoList()
    elif choice == "2":
        ExpenseTracker()
    elif choice == "3":
        ContactInfo()
    elif choice == "4":
        NoteBook()
    elif choice == "5":
        UtilitiesA()
    elif choice == "6":
        print("Exiting the personal organizer app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
