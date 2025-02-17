import functions
import time

while True:
    time_now = f"Today's time! ⭐ - {time.strftime("%H:%M - %d/%m/%Y")}"
    print(time_now)
    user_choice = input("Enter add, show, edit, complete or exit:").lower().strip()

    todos = functions.read_file()

    if user_choice.startswith("add"):
        todo = user_choice[4:]
        if todo != "":
            todo += "\n"
            todos.append(todo.title())
            functions.write_file(todos)
        else:
            print("Write something!")
    elif user_choice.startswith("show"):
        new_todos = [todo.strip('\n') for todo in todos]

        for index, todo in enumerate(new_todos):
            print(f"{index + 1} - {todo}")
    elif user_choice.startswith("edit"):
        try:
            todo = int(user_choice[4:])
            user_new_word = input("Write your new todo:") + "\n"
            todos[todo - 1] = user_new_word.title()
            functions.write_file(todos)
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
                functions.write_file(todos)
        except IndexError:
            print("The value is incorrect.")
            continue
        except ValueError:
            print("The command is invalid.")
            continue
    elif user_choice.startswith("exit"):
        print("Bye!")
        break
    else:
        print("Write a known command!")