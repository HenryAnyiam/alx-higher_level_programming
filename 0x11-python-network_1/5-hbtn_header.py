#!/usr/bin/python3
"""module using requests to send HTTP requests"""

import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
