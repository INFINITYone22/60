def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
