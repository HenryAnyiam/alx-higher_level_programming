#!/usr/bin/node
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
    return;
  }
  console.log(JSON.parse(body).title);
});
