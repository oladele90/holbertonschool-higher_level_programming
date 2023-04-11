#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 & h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let listy = '';
    for (let j = 0; j < this.width; j++) {
      listy += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(listy);
    }
  }

  rotate () {
    const tempWidth = this.width;
    this.width = this.height;
    this.height = tempWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
