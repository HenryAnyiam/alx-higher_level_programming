#!/bin/bash
#send a POST request with a query string
curl -sX POST -H "Content-Type:application/x-www-form-urlencoded&Content-Length:56"-d "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD" $1;
