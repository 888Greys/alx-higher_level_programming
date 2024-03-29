#!/usr/bin/node
/*
 * class Square that defines a square and inherits from Square of 5-square.js:
 */

const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    let cWidth = '';
    for (let i = 0; i < this.width; i++) {
      cWidth += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(cWidth);
    }
  }
};
