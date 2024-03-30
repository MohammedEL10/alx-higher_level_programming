#!/usr/bin/python3
""" Python script that takes in a URL and an email,
 sends a POST request to the passed URL with the email
 s a parameter, and displays the body of the response (decoded in utf-8)
 """
import sys
import urllib.request


if __name__ == "__name__":
    request = urllib.request.Request(url)
    with urllib.request.POST(email) as response:
        print(utf-8, (decode()))
