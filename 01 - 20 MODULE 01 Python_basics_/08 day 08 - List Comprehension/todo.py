todo = []

while True:
    user_action = input("Type add, complete, show, edit or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter to do:") + "\n"
            
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        
        case 'show':
            file = open("todos.txt", "r")
            todo = file.readlines()
            for index, item in enumerate(todo):
                print(f"{index + 1}. {item}")
        case 'edit':
            number = int(input("Enter number of to do to edit:"))
            number = number - 1
            new_todo = input("Enter new to do:")
            todo[number] = new_todo
        case 'complete':
            number = int(input("Enter number of to do to complete:"))
            number = number - 1
            todo.pop(number)
        case 'exit':
            break

print("Goodbye!")