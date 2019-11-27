import json


def read_tasks(file):
    """The function reads data from file."""
    with open(file) as fd:
        return json.loads(fd.read())


def write_tasks(file, tasks):
    """The function writes data to file."""
    with open(file, 'w') as fd:
        fd.write(json.dumps(tasks))


def show_tasks(file):
    """The function prints tasks in console."""
    tasks = read_tasks(file)
    print('\n\n{:^50}'.format('TASKS'))
    print('-' * 50)
    for index, task in enumerate(tasks):
        print('{0} | {1:<33} | {2}'.format(index, task['task'], task['deadline']))


def add_task(task, deadline, file):
    """The function adds task."""
    tasks = read_tasks(file)
    tasks.append({'task':task, 'deadline':deadline})
    write_tasks(file, tasks)
    return 0


def remove_task(index, file):
    """The function removes tasks."""
    tasks = read_tasks(file)
    if index < 0 or index > len(tasks) - 1: return -1
    del tasks[index]
    write_tasks(file, tasks)
    return 0


FILE = 'zad18.json'

while True:
    # Show task in console
    show_tasks(FILE)

    # Add task  or remove tasks or close program 
    action = input('\nEnter: "add" to add task, "remove" to remove task, "close" to close program: ')

    if action == 'add':
        task = input('Enter short tast: ')
        deadline = input('Enter deadline: ')
        if add_task(task, deadline, FILE) == 0:
            print('Task added!')
        else:
            print('There are some probelms!')        
    elif action == 'remove':
        try:
            index = int(input('Enter index of task: '))
            if remove_task(index, FILE) == -1:
                print('Select a number from the list!')
            else:
                print('Task removed!')
        except:
            print('Enter integer!')
    elif action == 'close':
        break
    else:
        print('Command not recognized')
