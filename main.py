message = "Enter a todo:"

todos = []

while True:
    todo = input(message)
    todos.append(todo.capitalize())
    print(todos)