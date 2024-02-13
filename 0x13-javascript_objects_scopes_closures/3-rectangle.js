#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 & h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h = this.height ? this.height : 0;
    const w = this.width ? this.width : 0;
    const out = 'X'.repeat(w);

    while (h) { console.log(out); h--; }
  }
}

module.exports = Rectangle;
