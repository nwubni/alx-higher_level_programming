#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    let output = '';

    if (c === undefined) { c = 'X'; }

    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) { output += c; }

      console.log(output);
      output = '';
    }
  }
};
