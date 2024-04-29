#!/usr/bin/node
/* script that prints a square, square size come from 1st argument
*/
let a;
let b;
let str = '';
if ((a = process.argv[2]) && (b = parseInt(a))) {
  for (let i = 0; i < b; i++) {
    str += 'X';
  }
  for (let i = 0; i < b; i++) {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
