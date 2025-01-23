todos = []

while True:
    user_choice = input("Enter add, show or exit:").lower().strip()

    match user_choice:
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo.capitalize())
        case "show":
            for todo in todos:
                print(todo)
        case "exit":
            print("Bye!")
            break
        case _:
            print("Write a known command!")
