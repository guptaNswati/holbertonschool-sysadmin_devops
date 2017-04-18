#!/usr/bin/python3
"""
This module using the given REST API, for a given employee ID, returns
information about his/her TODO list progress and export data in json format.
"""
import requests
import sys


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except (TyepError, Valuerror):
        print("Given id is invalid")
        sys.exit()
    req = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = []
    for task in req.json():
        if task.get('userId') == employee_id:
            tasks.append(task)

    req = requests.get("https://jsonplaceholder.typicode.com/users/")
    for user in req.json():
        if user.get('id') == employee_id:
            name = user.get('username')
    file_name = "{:d}.json".format(employee_id)
    with open(file_name, 'w') as f:
        f.write('{"' + str(employee_id) + '": [')
        for task in range(0, len(tasks) - 1):
            f.write('{"' + "task" + '": ' + '"' + tasks[task].get('title') +
                    '", ' + '"completed": ' + str(tasks[task].get('completed'))
                    + ", " + '"username": ' +  '"' + name + '"}, ')
        f.write('{"' + "task" + '": ' + '"' + tasks[task].get('title') + '", '
                + '"completed": ' + str(tasks[task].get('completed')) + ", "
                + '"username": ' +  '"' + name + '"}]}')
