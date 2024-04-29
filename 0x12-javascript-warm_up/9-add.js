#!/usr/bin/node
/* script that prints the addition of 2 integers
*/
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
let a;
let b;
if ((a = process.argv[2]) && (b = process.argv[3])) {
  console.log(add(a, b));
} else {
  console.log('NaN');
}
