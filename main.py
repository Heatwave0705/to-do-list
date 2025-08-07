tasks = {}

def main_menu():
    choice = input(
        "1. Add a new task\n"
        "2. Delete a task\n"
        "3. Mark a task down\n"
        "4. Delete all complete tasks\n"
        "5. See all tasks\n"
        "Enter your choice (number 1-5): "
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

def print_tasks():
    print("\n")
    print (tasks)

def starting_prompt():
    match main_menu():
        case "1":
            new_task()
        case "2":
            delete_task()
        case "3":
            mark_down()
        case "4":
            delete_complete_tasks()
        case "5":
            print_tasks()
        case _:
            print("\nThat is not an integer between 1-5, please try again\n")
            starting_prompt()

def ending_prompt():
    match input("\nWould you like to exit the program (enter '1') or go back to the main menu (enter '2')? "):
        case "1":
            quit()
        case "2":
            main()
        case _:
            print("Sorry, that's not an option, please try again")
            ending_prompt()

def main():
    starting_prompt()
    ending_prompt()

if __name__ == "__main__":
    main()
