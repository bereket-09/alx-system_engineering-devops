#!/usr/bin/python3
"""
<<<<<<< HEAD
<<<<<<< HEAD
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
=======
=======
>>>>>>> parent of d59d8ae... Update 0-gather_data_from_an_API.py
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import re
<<<<<<< HEAD
>>>>>>> parent of d59d8ae... Update 0-gather_data_from_an_API.py
=======
>>>>>>> parent of d59d8ae... Update 0-gather_data_from_an_API.py
import requests
from sys import argv


<<<<<<< HEAD
<<<<<<< HEAD
if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
=======
=======
>>>>>>> parent of d59d8ae... Update 0-gather_data_from_an_API.py

API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API, id)).json()
            todos_res = requests.get('{}/todos'.format(API)).json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            todos_done = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user_name,
                    len(todos_done),
                    len(todos)
                )
            )
            for todo_done in todos_done:
                print('\t {}'.format(todo_done.get('title')))
<<<<<<< HEAD
>>>>>>> parent of d59d8ae... Update 0-gather_data_from_an_API.py
=======
>>>>>>> parent of d59d8ae... Update 0-gather_data_from_an_API.py
