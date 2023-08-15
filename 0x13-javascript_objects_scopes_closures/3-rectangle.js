#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let myW = 'X';
    let i;
    if (!(isNaN(this.width))) {
      for (i = 1; i < this.width; i++) {
        myW += 'X';
      }
      for (i = 0; i < this.height; i++) {
        console.log(myW);
      }
    }
  }
};
module.exports = Rectangle;
