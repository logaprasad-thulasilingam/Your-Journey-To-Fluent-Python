import argparse

def list_TASKS(TASKS):
    if len(TASKS) != 0:
        for item in TASKS:
            print (item)
    else:
        print("No Tasks Available")

def update_TASKS (operation):
    if operation == "add":
        task = input("Enter the task to add:")
        TASKS.append(task)
        print("Task Updated")
    elif operation == "delete":
        pass

TASKS = []
parser = argparse.ArgumentParser()
# parser.add_argument("add", help = "Add new task")
# parser.add_argument("delete", help = "Delete existing task")
parser.add_argument("--operation", help = "Add or Remove a task from manager", choices=["add", "delete"])
parser.add_argument("--list", help = "List all tasks", action="store_true")
args = parser.parse_args()

if args.operation == "add":
    update_TASKS("add")
elif args.operation == "delete":
    update_TASKS("delete")

if args.list:
    list_TASKS(TASKS)



