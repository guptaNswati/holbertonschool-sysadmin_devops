#!/usr/bin/python3
"""
This module using the given REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get("https://jsonplaceholder.typicode.com/users/")
    for employee in req.json():
        if employee.get('id') == int(sys.argv[1]):
            print(employee)
            break
