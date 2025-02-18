import functions
import FreeSimpleGUI as sg

# Reading file
todos = functions.read_file()

text = sg.Text("Type in a todo")
todo = sg.Input(tooltip="Write a todo here.", key="todo")
button = sg.Button('Add')

# Create the window
window = sg.Window('My ToDo App', layout=[[text], [todo], [button]])

events, values = window.read()
todo_text = values["todo"] + "\n"
print_text = values["todo"]

# Writing file
todos.append(todo_text)
functions.write_file(todos)

print(f"The {print_text} was added with success!")

window.close()
