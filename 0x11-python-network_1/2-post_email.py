#!/usr/bin/python3
"""module to use urllib.request module"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == '__main__':
    data = {'email' : argv[2]}
    data = urlencode(data)
    data = data.encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as respose:
        res = response.read().decode('utf-8')
    print(res)
