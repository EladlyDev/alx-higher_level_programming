#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let h = this.height;
      const w = this.width;
      const out = c.repeat(w);

      while (h) { console.log(out); h--; }
    } else { this.print(); }
  }
}

module.exports = Square;
