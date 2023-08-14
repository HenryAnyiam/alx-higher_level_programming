#!/usr/bin/node
const { argv } = require('process');
let length = 0;
argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  length++;
});
if (length === 2) {
  console.log('No argument');
}
