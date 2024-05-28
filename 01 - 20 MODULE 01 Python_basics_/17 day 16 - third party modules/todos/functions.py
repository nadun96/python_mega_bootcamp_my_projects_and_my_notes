FILEPATH = r"E:\Portfolio\UDEMY\CURRENT\Python mega\s17 day 16 - third party modules\todos\todos.txt"


def get_todos(filepath=FILEPATH):
    """Read the content of the file
    and return list of to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the todo items list in the text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("functions module is running as a script")
    print(get_todos())
