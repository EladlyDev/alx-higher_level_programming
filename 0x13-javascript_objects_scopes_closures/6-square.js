#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
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
