#!/usr/bin/node
const { argv } = require('process');
const length = argv.length;
if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
