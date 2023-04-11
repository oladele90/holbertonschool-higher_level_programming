#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
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
