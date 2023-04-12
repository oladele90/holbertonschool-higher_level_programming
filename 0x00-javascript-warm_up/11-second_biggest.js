#!/usr/bin/node
if (isNaN(process.argv[3])) {
  console.log('0');
} else {
  const arr = [];
  let j = 0;
  for (let i = 2; i < process.argv.length; i++) {
    arr[j] = Number(process.argv[i]);
    j++;
  }
  let max = -Infinity; let result = -Infinity;

  for (const value of arr) {
    const nr = Number(value);
    if (nr > max) {
      [result, max] = [max, nr];
    } else if (nr < max && nr > result) {
      result = nr;
    }
  }
  console.log(arr);
  console.log(result);
}
