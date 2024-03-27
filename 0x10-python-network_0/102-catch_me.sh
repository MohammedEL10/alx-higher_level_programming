#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -sX $1 -H "0.0.0.0:5000/catch_me: You got me!" -L -d @$2 -L
