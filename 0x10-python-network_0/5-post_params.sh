#!/bin/bash
#send a POST request with a query string
curl -sX POST -d "email=test@gmail%2Ecom&subject=I will always be here for PLD" $1;
