from dataclasses import replace

todos = []

while True:
    user_choice = input("Enter add, show, edit or exit:").lower().strip()

    match user_choice:
        case "add":
            todo = input("Enter a todo:")
            todos.append(todo.title())
        case "show":
            for index, todo in enumerate(todos):
                print(index + 1, "-", todo)
        case "edit":
            user_edit_choice = int(input("Write the number of the todo:"))
            user_new_word = input("Write your new todo:")
            new_todo = todos[user_edit_choice - 1] = user_new_word.title()
        case "exit":
            print("Bye!")
            break
        case _:
            print("Write a known command!")
