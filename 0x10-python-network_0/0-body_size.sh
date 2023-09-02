#!/usr/bin/bash
#takes a URL, sends a request to it and displays the size
curl -s -o output.html -w "%{size_download}" $1;
