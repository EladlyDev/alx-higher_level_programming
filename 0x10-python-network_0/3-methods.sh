#!/bin/bash
# displays all HTTP methods the server will accept.
curl -siX OPTIONS "$1" | grep -oP "(?<=Allow: )(?:\w+,? ?)+"
