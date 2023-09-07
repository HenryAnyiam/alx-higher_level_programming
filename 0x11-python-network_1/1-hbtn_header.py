#!/usr/bin/python3
"""module to use urllib.request module"""

from urllib.request import Request, urlopen
from sys import argv


if __name__ == '__main__':
    req = Request(argv[1])
    with urlopen(req) as response:
        headers = response.info()
    print(headers.get('X-Request-Id'))
