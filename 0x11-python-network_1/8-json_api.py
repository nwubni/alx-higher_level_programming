#!/usr/bin/python3
"""
Search API
"""
import sys
import requests


if __name__ == "__main__":
    alpha = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": alpha}

    result = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = result.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
