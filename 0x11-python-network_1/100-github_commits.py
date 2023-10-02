#!/usr/bin/python3
"""Time for an interview!"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)
    git_commits = req.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                git_commits[i].get("sha"),
                git_commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
