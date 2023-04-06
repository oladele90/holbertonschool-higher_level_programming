#!/usr/bin/node
function fact (a, factory) {
  if (a < 0) {
    return (-1);
  }
  if (a === 0) {
    return (1);
  }
  return (a * fact(a - 1));
}
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(fact(parseInt(process.argv[2])));
}
