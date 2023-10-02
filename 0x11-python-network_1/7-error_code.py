#!/usr/bin/python3
"""Error code #1"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
        sys.exit(1)

    print(req.text)
