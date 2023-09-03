#!/bin/bash
#send an OPTIONS request
curl -sI $1 | grep 'Allow' | cut -d " " -f2-
