#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)

    print(req.json().get("id"))
