import os

TODO_FILE="todo_list.txt"

tasks=[]

def loadTasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE,'r') as file:
        return file.read().splitlines()

def saveTasks(tasks):
    with open(TODO_FILE,"w") as file:
        file.write("\n".join(tasks))


def addTask():
    tasks=loadTasks()
    task=input("Enter a task :")
    tasks.append(task)
    saveTasks(tasks)
    print(f"Task '{task}' is added to the list")

def viewTasks():
    tasks=loadTasks()
    if not tasks:
        print("There are no tasks")
    else:
        print("Current tasks")
        for index, task in enumerate(tasks):
            print(f"Tasks #{index}.{task}")

def deleteTask():
    tasks=loadTasks()
    try:
        tasktoDelete = int(input("Enter # to delete:"))
        if tasktoDelete >=0 and tasktoDelete < len(tasks):
            tasks.pop(tasktoDelete-1)
            saveTasks(tasks)
            print(f"Task {tasktoDelete-1} has been deleted")
        else:
            print(f"The task {tasktoDelete} was not found")
    except ValueError:
        print("Invalid input")
                           

if __name__=="__main__":
    print("Welcome to the TODO list App")
    while True:
        print("\n")
        print("Please Select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. view Tasks")
        print("3. Delete a task")
        print("4.Quit")
        
        choice=input("Enter your Choice :")

        if (choice == "1" ):
            addTask()
        elif (choice == "2"):
            viewTasks()
        elif (choice == "3"):
            deleteTask()
        elif (choice == "4") :
            break
        else:
            print("Invalid input")
print("Goodbye mate")




     