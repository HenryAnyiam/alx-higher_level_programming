#!/usr/bin/python3
"""module to use urllib.request module"""

from urllib.request import Request, urlopen


if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        data = response.read()
    print(f"Body response:\n    - type: {type(data)}")
    print(f"    - content: {data}\n    - utf8 content: {data.decode('utf-8')}")
