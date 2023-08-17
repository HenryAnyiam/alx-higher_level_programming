#!/usr/bin/node
const square = require('./5-square');
const Square = class extends square {
  charPrint (c) {
    let i;
    let myChar = 'X';
    let myC = 'X';
    if (!(c === undefined)) {
      myChar = c;
      myC = c;
    }
    if (!(isNaN(this.width))) {
      for (i = 1; i < this.width; i++) {
        myChar += myC;
      }
      for (i = 0; i < this.width; i++) {
        console.log(myChar);
      }
    }
  }
};
module.exports = Square;
