#!/bin/bash
# Gets the size of the body of a response from a URL
curl -sI "$1" | grep -iE 'Content-Length:' | awk '{print $2}'
