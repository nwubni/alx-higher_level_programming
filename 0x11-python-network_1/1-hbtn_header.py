#!/usr/bin/python3
"""Response header value #0
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
