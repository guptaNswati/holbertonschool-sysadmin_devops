#!/usr/bin/python3
"""
This module using the given REST API, for a given employee ID, returns
information about his/her TODO list progress.
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
    completed = 0
    total = 0
    done_tasks = []
    for task in req.json():
        if task.get('userId') == employee_id:
            total += 1
            if task.get('completed'):
                completed += 1
                done_tasks.append(task.get('title'))
    
    req = requests.get("https://jsonplaceholder.typicode.com/users/")
    for employee in req.json():
        if employee.get('id') == employee_id:
            name = employee.get('name')
            break

    print("Employee {:s} is done with tasks({:d}/{:d}):".format(
        name, completed, total))
    for task in done_tasks:
        print(task)
