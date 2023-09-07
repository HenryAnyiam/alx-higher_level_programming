#!/usr/bin/python3
"""module to use urllib.request module"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv


if __name__ == '__main__':
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
