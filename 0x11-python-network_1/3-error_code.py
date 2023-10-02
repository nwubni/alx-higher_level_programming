#!/usr/bin/python3
"""Error code #0
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            decoded = res.read().decode("utf-8")
            print(decoded)
    except error.HTTPError as err:
        print('Error code:', err.code)
