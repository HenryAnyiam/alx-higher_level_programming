#!/usr/bin/node
const { argv } = require('process');
const myArray = argv.slice(2);
const length = argv.length;
if (length < 4) {
  console.log(0);
} else {
  myArray.sort(function (a, b) { return (a - b); });
  console.log(myArray[myArray.length - 1]);
}
