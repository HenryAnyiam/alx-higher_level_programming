#!/usr/bin/python3
"""module using requests to send HTTP requests"""

import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(res.text)}\n\t- content: {res.text}")
