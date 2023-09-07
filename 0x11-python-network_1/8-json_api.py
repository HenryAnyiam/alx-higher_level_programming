#!/usr/bin/python3
"""
module using requests to send HTTP requests
sends a POST request http://0.0.0.0:5000/search_user
"""

import requests
from sys import argv


if __name__ == "__main__":
    val = ""
    if len(argv) == 2:
        val = argv[1]
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': val})
    try:
        data = res.json()
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
    else:
        if len(data) > 0:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print('No result')
