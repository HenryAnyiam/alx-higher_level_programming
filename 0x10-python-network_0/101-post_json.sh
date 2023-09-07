#!/bin/bash
#send a POST JSON request
curl -sX POST -d @$2 -H "Content-Type: application/json" $1
