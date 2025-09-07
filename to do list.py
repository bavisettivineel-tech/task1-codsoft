def main():
    tasks = []
    while True:
        print("\n===== To-Do List =====")
        print("1. Add tasks\n2. Show tasks\n3. Mark as done\n4. Exit")
        ch = input("Enter your choice: ")
        if ch == "1":
            n_tasks = int(input("How many tasks you want to add: "))
            for i in range(n_tasks):
                task = input("Enter your task: ")
                tasks.append({"task": task, "done": False})
                print("Task added")
        elif ch == "2":
            print("\nTASKS:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")
        elif ch == "3":
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number")
        elif ch == "4":
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()