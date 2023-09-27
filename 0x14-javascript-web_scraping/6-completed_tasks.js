#!/usr/bin/node
const request = require('request');
const result = {};
let data;
let id = 1;
let count = 0;
let i;

request.get(process.argv[2], function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
    return;
  }
  data = JSON.parse(body);
  for (i in data) {
    if (data[i].userId === id) {
      if (data[i].completed === true) {
        count += 1;
      }
    } else {
      result[id] = count;
      id += 1;
      count = 0;
    }
  }
  result[id] = count;
  console.log(result);
});
