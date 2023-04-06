#!/usr/bin/node
let listy = '';
let x = parseInt(process.argv[2]);
let go = true;
for (let i = x; i > 0; i--) {
  listy += 'X';
}
while (go === true) {
  if (x > 0) {
    console.log(listy);
    x -= 1;
  } else {
    go = false;
  }
}
if (!process.argv[2] || (!Number.isInteger(x))) {
  console.log('Missing size');
}
