#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row;
    let i;
    row = '';
    for (i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
