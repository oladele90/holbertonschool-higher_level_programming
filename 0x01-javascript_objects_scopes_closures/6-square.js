#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let listy = '';
      for (let j = 0; j < this.width; j++) {
        listy += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(listy);
      }
    } else {
      super.print();
    }
  }
};
