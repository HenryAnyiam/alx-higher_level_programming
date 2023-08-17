#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');
const length = argv.length;
if (length === 5) {
  fs.readFile(argv[2], 'utf-8', (err, data) => {
    if (!(err)) {
      fs.writeFile(argv[4], data, 'utf-8', err => {
      if (err) {
      return;
      }
      });
    }
  });
  fs.readFile(argv[3], 'utf-8', (err, data) => {
    if (!(err)) {
      fs.appendFile(argv[4], data, 'utf-8', err => {
      if (err) { 
      return; 
      }
      });
    }
  });
}
