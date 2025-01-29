def write_file():
    with open("todos.txt", "w") as text_file:
        text_file.writelines(todos)

while True:
    user_choice = input("Enter add, show, edit, complete or exit:").lower().strip()

    with open("todos.txt", "r") as file:
        todos = file.readlines()

    match user_choice:
        case "add":
            todo = input("Enter a todo:") + "\n"
            todos.append(todo.title())
            write_file()
        case "show":
            new_todos = [todo.strip('\n') for todo in todos] # List Comprehension

            for index, todo in enumerate(new_todos):
                # todo = todo.strip("\n")
                print(f"{index + 1} - {todo}")
        case "edit":
            user_edit_choice = int(input("Write the number of the todo:"))
            user_new_word = input("Write your new todo:") + "\n"
            new_todo = todos[user_edit_choice - 1] = user_new_word.title()
            write_file()
        case "complete":
            user_complete_choice = int(input("Which todo do you want to complete?"))
            todos.pop(user_complete_choice - 1)
            write_file()
        case "exit":
            print("Bye!")
            break
        case _:
            print("Write a known command!")
