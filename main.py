def write_file():
    with open("todos.txt", "w") as text_file:
        text_file.writelines(todos)

while True:
    user_choice = input("Enter add, show, edit, complete or exit:").lower().strip()


    with open("todos.txt", "r") as file:
        todos = file.readlines()

    if user_choice.startswith("add"):
        todo = user_choice[4:]
        if todo != "":
            todo += "\n"
        # todo = input("Enter a todo:") + "\n"
            todos.append(todo.title())
            write_file()
    elif user_choice.startswith("show"): # Doesn't need more than this word.
        new_todos = [todo.strip('\n') for todo in todos] # List Comprehension

        for index, todo in enumerate(new_todos):
            # todo = todo.strip("\n")
            print(f"{index + 1} - {todo}")
    elif user_choice.startswith("edit"):
        try:
            todo = int(user_choice[4:])
            # print(todo)
            # user_edit_choice = int(input("Write the number of the todo:"))
            user_new_word = input("Write your new todo:") + "\n"
            todos[todo - 1] = user_new_word.title() # Python allows two attribution? Yes! but doesn't look good.
            write_file()
        except ValueError:
            print("The command is incorrect.")
            continue
    elif user_choice.startswith("complete"):
        try:
            todo = int(user_choice[8:]) - 1
            # print(todo)
            if todo != "":
                # user_complete_choice = int(input("Which todo do you want to complete?"))
                # index = user_complete_choice - 1
                remove_item = todos[todo].strip("\n")
                todos.pop(todo)
                print(f"The todo {remove_item} was removed.")
                write_file()
        except IndexError:
            print("The value is incorrect.")
            continue
    elif user_choice.startswith("exit"):
        print("Bye!")
        break
    else:
        print("Write a known command!")
    # case _:
    #     print("Write a known command!")


# The program won't check another conditionals with elif when executing one. It's good to save memory.