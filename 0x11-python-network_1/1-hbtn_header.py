#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        url = argv[1]
        req = Request(url)

        try:
            with urlopen(req) as response:
                x_request_id = response.headers.get("X-Request-Id")
                if x_request_id:
                    print(x_request_id)
                else:
                    print("X-Request-Id header not found in the response.")
        except URLError as e:
            print(f"Error: {e}")
        except HTTPError as e:
            print(f"HTTP Error: {e}")
