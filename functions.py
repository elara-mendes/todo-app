def write_file(todos_arg, filepath="todos.txt"):
    """
    Write the text file.
    """
    with open(filepath, "w") as text_file:
        text_file.writelines(todos_arg)

def read_file(filepath="todos.txt"):
    """
    Read the text file and return it.
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

# print("Outside text")
if __name__ == "__main__":
    print(help(read_file))
