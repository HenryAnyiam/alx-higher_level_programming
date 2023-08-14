#!/usr/bin/node
const { argv } = require('process');
const length = Number(argv[2]);
let i;
if (!(isNaN(length))) {
  for (i = 0; i < length; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
