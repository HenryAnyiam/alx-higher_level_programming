#!/usr/bin/node
const request = require('request');
let data;
let newData;
let i;

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
    return;
  }
  data = JSON.parse(body);
  for (i in data.characters) {
    request.get(data.characters[i], function (error, response, body) {
      if (error != null) {
        console.error('error:', error);
        return;
      }
      newData = JSON.parse(body);
      console.log(newData.name);
    });
  }
});
