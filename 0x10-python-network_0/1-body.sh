#!/usr/bin/bash
#takes a URL, sends a request to it and displays the size
if [ $# -eq 1 ]
then
	curl -s -L $1;
fi
