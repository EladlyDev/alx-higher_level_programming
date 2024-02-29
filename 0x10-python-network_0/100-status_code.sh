#!/bin/bash
# displays only the status code of the response.
curl -sI "$1" -w "%{response_code}" -o /dev/null
