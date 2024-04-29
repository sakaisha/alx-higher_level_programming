#!/usr/bin/node
/* prints x times “C is fun”, x from the first argument
*/
let a;
let b;
if ((a = process.argv[2]) && (b = parseInt(a))) {
  for (let i = 0; i < b; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
