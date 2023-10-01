#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header.

Usage: ./5-hbtn_header.py <URL>
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
    else:
        url = argv[1]
        try:
            req = requests.get(url)
            req.raise_for_status()  # Raise an exception if the response status is not 2xx
            x_request_id = req.headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
