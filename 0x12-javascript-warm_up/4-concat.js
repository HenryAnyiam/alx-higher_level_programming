#!/usr/bin/node
const { argv } = require('process');
const myVar = argv[2] + ' is ' + argv[3];
console.log(myVar);
