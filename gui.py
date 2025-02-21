import functions
import FreeSimpleGUI as sg


# Reading file
todos = functions.read_file()

text = sg.Text("Type in a todo")
todo = sg.Input(tooltip="Write a todo here.", key="todo")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=todos, enable_events=True, size=(45, 10), key="list_item")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Create the window
window = sg.Window('My ToDo App',
                   layout=[[text], [todo, add_button], [list_box, edit_button, complete_button],
                           [exit_button]])

while True:
    events, values = window.read()

    match events:
        case "Add":
            todo_text = values["todo"] + "\n"
            print_text = values["todo"]

            # Writing file
            todos.append(todo_text)
            functions.write_file(todos)

            window["todo"].update("")
            window["list_item"].update(values=todos)

            print(f"The {print_text} was added with success!")
        case "Edit":
            edit_todo = values["list_item"][0]
            new_todo = values["todo"]

            # Getting Index and writing file
            index_todo = todos.index(edit_todo)
            todos[index_todo] = new_todo + "\n"
            functions.write_file(todos)

            window["todo"].update("")
            window["list_item"].update(values=todos)
        case "Complete":
            complete_todo = values["list_item"][0]
            todos.remove(complete_todo)
            functions.write_file(todos)

            window["list_item"].update(values=todos)
    if events == sg.WIN_CLOSED or events == 'Exit':
        break

    print(events)
    print(values)

window.close()
