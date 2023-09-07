#!/usr/bin/python3
"""module using requests to send HTTP requests"""

import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
