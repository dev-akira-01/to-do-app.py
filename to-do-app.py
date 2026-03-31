#initiate

tasks= [] #empty list

def menu():
    print("1. Add New Task")
    print("2. Remove a Task")
    print("3. Mark a Task as Done")
    print("4. View all Tasks")
    print("5. Exit the Program")

def add_task():
    task= input("Enter task to be added: ")
    tasks.append({"tasks":task,"done":False})
    print(f"'{task}' was added successfully!")

def view_task():
    if not tasks: 
        print("There are no tasks added yet!")
        return
    print("\nYour tasks: ")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✕"
        print(f"{index}. {task['tasks']} [{status}]")


while True:
    menu()
    choice= input("Enter your Choice (1-5): ")
    try:
        if choice == "1":
            add_task()
        elif choice == "4":
            view_task()
        else: 
            print("Please enter a valid number")
    except:
        print("An unexpected error occured")

