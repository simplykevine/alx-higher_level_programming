#!/usr/bin/python3
"""Prints the GitHub id of a user."""
import sys
import requests
import base64

if __name__ == '__main__':
    if len(sys.argv) > 2:
        url = "https://api.github.com/user"
        username = sys.argv[1]
        password = sys.argv[2]

        # Encode the username and password (or personal access token) in Base64
        credentials = '{}:{}'.format(username, password)
        encoded_credentials = base64.b64encode(
            credentials.encode('utf-8')).decode('utf-8')

        req_headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'Basic {}'.format(encoded_credentials),
        }
        response = requests.get(url, headers=req_headers)

        if response.status_code == 200:
            user = response.json()

            if user.get('login') == username:
                print(user.get('id'))
            else:
                print('None')
        else:
            print('None')
