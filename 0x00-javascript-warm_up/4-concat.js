#!/usr/bin/node
const args = process.argv;
let args1 = '';
let args2 = '';
if (args[2]) {
  args1 = args[2];
} else {
  args1 = 'undefined';
}
if (args[3]) {
  args2 = args[3];
} else {
  args2 = 'undefined';
}
console.log(args1 + ' is ' + args2);
