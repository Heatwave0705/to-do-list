tasks = {}

def main_menu():
    choice = input(
        '\n'
        "1. Add a new task\n"
        "2. Delete a task\n"
        "3. Mark a task down\n"
        "4. Delete all complete tasks\n"
        "5. See all tasks\n"
        "6. Exit program\n"
        "Enter your choice (number 1-6): "
    )

    return choice
def new_task():
    tasks.update({input("What task would you like to enter? ").lower().capitalize(): "Incomplete"})

def delete_task():
    tasks.pop(input("Which task would you like to delete? ").lower().capitalize())

def mark_down():
    tasks[input("Which task would you like to mark as complete? ").lower().capitalize()] = "Complete"

def delete_complete_tasks():
    for task in list(tasks.keys()):
        if tasks[task] == "Complete":
            tasks.pop(task)
print("Blue")
def print_tasks():
    print("\n")
    print (tasks)

def starting_prompt():
    match main_menu():
        case "1":
            new_task()
            main()
        case "2":
            delete_task()
            main()
        case "3":
            mark_down()
            main()
        case "4":
            delete_complete_tasks()
            main()
        case "5":
            print_tasks()
            main()
        case "6":
            quit()
        case _:
            print("\nThat is not an integer between 1-6, please try again\n")
            starting_prompt()


def main():
    starting_prompt()

if __name__ == "__main__":
    main()
