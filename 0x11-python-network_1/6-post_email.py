#!/usr/bin/python3
"""module using requests to send HTTP requests"""

import requests
from sys import argv


if __name__ == "__main__":
    res = requests.post(argv[1], data={'email': argv[2]})
    print(res.text)
