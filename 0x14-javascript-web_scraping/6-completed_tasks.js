#!/usr/bin/node
const request = require('request');
const result = {};
let data;
let id;
let count = 0;
let i;

request.get(process.argv[2], function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
    return;
  }
  data = JSON.parse(body);
  id = data[0].userId;
  for (i in data) {
    if (data[i].userId === id) {
      if (data[i].completed === true) {
        count += 1;
      }
    } else {
      result[id] = count;
      id = data[i].userId;
      count = 0;
      if (data[i].completed === true) {
        count += 1;
      }
    }
  }
  result[id] = count;
  console.log(result);
});
