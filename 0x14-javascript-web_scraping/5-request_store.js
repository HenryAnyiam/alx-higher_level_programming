#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
