#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
response=$(curl -sI $1 | grep -i "Content-Length" | awk '{print $2}')
if [ -n "$response" ]; then
    echo "Content-Length: $response bytes"
else
    echo "Content-Length not found in the response headers."
fi
