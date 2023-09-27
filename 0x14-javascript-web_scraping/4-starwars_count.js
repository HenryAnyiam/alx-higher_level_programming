#!/usr/bin/node
const request = require('request');
let data;
let i;
let j;
let count = 0;

request.get(process.argv[2], function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
    return;
  }
  data = JSON.parse(body);
  for (i in data.results) {
    for (j in data.results[i].characters) {
      if (data.results[i].characters[j].includes('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
