#!/bin/bash
# Retrieves the status code of a request sent to a given URL
curl -s -w "%{response_code}" -o /dev/null "$1"
