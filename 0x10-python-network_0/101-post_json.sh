#!/bin/bash
#send a POST JSON request
curl -sX POST -d @$1 -H "Content-Type: application/json" $2
