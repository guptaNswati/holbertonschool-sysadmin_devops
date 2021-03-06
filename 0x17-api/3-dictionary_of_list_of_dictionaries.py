#!/usr/bin/python3
"""
This module using the given REST API, for all employees, returns
information about his/her TODO list progress and export data in json format.
"""
import os
import requests


if __name__ == "__main__":
    users = []
    file_name = "todo_all_employees.json"
    req = requests.get("https://jsonplaceholder.typicode.com/users/")
    for user in req.json():
        u = [user.get('id'), user.get('username')]
        users.append(u)
    req = requests.get("https://jsonplaceholder.typicode.com/todos")
    with open(file_name, 'w') as f:
        for user in users:
            f.write('{"' + str(user[0]) + '": [')
            for task in req.json():
                if user[0] == int(task.get('userId')):
                    f.write('{"username' + '": ' + '"' + str(user[1]) +
                            '", ' + '"task": ' + '"' + task.get(
                                'title') + '", ' + '"completed": ' +
                            str(task.get('completed')) + ", ")
    with open(file_name, 'rb+') as f:
        f.seek(-2, os.SEEK_END)
        f.truncate()
    with open(file_name, 'a') as f:
        f.write("}]}")
