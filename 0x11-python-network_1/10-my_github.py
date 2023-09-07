#!/usr/bin/python3
"""module using requests to send HTTP requests"""

import requests
from sys import argv


if __name__ == "__main__":
    try:
        res = requests.get(f'https://api.github.com/users/{argv[1]}',
                           auth=(argv[1], argv[2]))
    except requests.exceptions.ConnectionError:
        print('None')
    else:
        try:
            data = res.json()
        except requests.exceptions.JSONDecodeError:
            print('None')
        else:
            if 'id' in data:
                print(data.get('id'))
            else:
                print('None')
