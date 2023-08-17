#!/usr/bin/node
const dict = require('./101-data').dict;
const keys = Object.keys(dict);
const values = Object.values(dict);
const length = keys.length;
const myDict = {};
let i;
for (i = 0; i < length; i++) {
  if (values[i] in myDict) {
    myDict[values[i]].push(keys[i]);
  } else {
    myDict[values[i]] = [keys[i]];
  }
}
console.log(myDict);
