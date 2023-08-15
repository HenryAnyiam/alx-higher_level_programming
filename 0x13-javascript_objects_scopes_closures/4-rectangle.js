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

  double () {
    if (!(isNaN(this.width))) {
      this.width *= 2;
      this.height *= 2;
    }
  }

  rotate () {
    const myW = this.width;
    const myH = this.height;
    if (!(isNaN(this.width))) {
      this.width = myH;
      this.height = myW;
    }
  }
};
module.exports = Rectangle;
