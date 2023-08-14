#!/usr/bin/node
const { argv } = require('process');
const myNum = Number(argv[2]);
if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
