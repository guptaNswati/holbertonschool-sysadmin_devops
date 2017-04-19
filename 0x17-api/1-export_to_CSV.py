#!/usr/bin/python3
"""
This module using the given REST API, for a given employee ID, returns
information about his/her TODO list progress and export data in the CSV format.
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
    for employee in req.json():
        if employee.get('id') == employee_id:
            name = employee.get('name')
            break
    file_name = "{:d}.csv".format(employee_id)
    with open(file_name, 'w') as f:
        for task in tasks:
            f.write('"' + str(employee_id) + '"' + "," + '"' + name + '"' +
                    "," + '"' + str(task.get('completed')) + '"' + "," +
                    '"' + task.get('title') + '"' + "\n")
