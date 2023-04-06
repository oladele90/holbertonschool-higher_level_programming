#!/usr/bin/node
const listy = 'C is fun';
let x = parseInt(process.argv[2]);
let go = true;
while (go === true) {
  if (x > 0) {
    console.log(listy);
    x -= 1;
  } else {
    go = false;
  }
}
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
}
