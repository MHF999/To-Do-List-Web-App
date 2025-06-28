FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Return the list of to-do items from a text file."""

    with open(filepath, 'r') as file:
        todos = file.readlines()
        todos = [todo.strip() for todo in todos]
    
    return todos


def write_todos(todos, filepath=FILEPATH):
    """Write the list of to-do items in a text file."""

    with open(filepath, 'w') as file:
        todos = [todo + '\n' for todo in todos]
        file.writelines(todos)
    

if __name__ == "__main__":
    print("functions.py was executed directly.")