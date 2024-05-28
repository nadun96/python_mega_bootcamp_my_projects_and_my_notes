import functions
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print('It is',now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos(todo)

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, todo in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            