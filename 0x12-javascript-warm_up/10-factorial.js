#!/usr/bin/node
/* script that computes and prints a factorial
*/
function factorial (num) {
  if (num === 0) {
    return 0;
  } else if (!num || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
let value = process.argv[2];
let num = parseInt(value);
console.log(factorial(num));
