#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let output = '';

    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) { output += 'X'; }

      console.log(output);
      output = '';
    }
  }

  rotate () {
    const t = this.height;
    this.height = this.width;
    this.width = t;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
