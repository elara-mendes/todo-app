def write_file(filepath, todos_arg):
    with open(filepath, "w") as text_file:
        text_file.writelines(todos_arg)

def read_file(filepath):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


while True:
    user_choice = input("Enter add, show, edit, complete or exit:").lower().strip()

    todos = read_file("todos.txt")

    if user_choice.startswith("add"):
        todo = user_choice[4:]
        if todo != "":
            todo += "\n"
            todos.append(todo.title())
            write_file("todos.txt", todos)
    elif user_choice.startswith("show"):
        new_todos = [todo.strip('\n') for todo in todos]

        for index, todo in enumerate(new_todos):
            print(f"{index + 1} - {todo}")
    elif user_choice.startswith("edit"):
        try:
            todo = int(user_choice[4:])
            user_new_word = input("Write your new todo:") + "\n"
            todos[todo - 1] = user_new_word.title()
            write_file("todos.txt", todos)
        except ValueError:
            print("The command is incorrect.")
            continue
    elif user_choice.startswith("complete"):
        try:
            todo = int(user_choice[8:]) - 1
            if todo != "":
                remove_item = todos[todo].strip("\n")
                todos.pop(todo)
                print(f"The todo {remove_item} was removed.")
                write_file("todos.txt", todos)
        except IndexError:
            print("The value is incorrect.")
            continue
    elif user_choice.startswith("exit"):
        print("Bye!")
        break
    else:
        print("Write a known command!")