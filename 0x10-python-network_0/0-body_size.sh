#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep -Ei 'Content-Length: [0-9]+' | grep -oE '[0-9]+'
