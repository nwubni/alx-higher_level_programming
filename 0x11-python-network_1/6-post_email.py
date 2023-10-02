#!/usr/bin/python3
"""POST an email #1
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    data_value = {"email": sys.argv[2]}
    req = requests.post(url, data=data_value)

    print(req.text)
