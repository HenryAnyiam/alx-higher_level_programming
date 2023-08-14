#!/usr/bin/node
const { argv } = require('process');
const length = Number(argv[2]);
let i, line;
line = 'X';
if (!(isNaN(length))) {
  for (i = 1; i < length; i++) {
    line += 'X';
  }
  for (i = 0; i < length; i++) {
    console.log(line);
  }
} else {
  console.log('Missing size');
}
