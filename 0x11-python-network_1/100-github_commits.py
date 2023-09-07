#!/usr/bin/python3
"""module using requests to send HTTP requests"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res = get(f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits')
    data = res.json()
    top = data[:10]
    for i in top:
        sha = i.get('sha')
        name = i.get('commit').get('author').get('name')
        print(f'{sha}: {name}')
