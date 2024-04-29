#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments
*/
let len = process.argv.length;
let first;
let second;
let check = 1;
if (len <= 3) {
  console.log(0);
} else {
  let arr = process.argv;
  first = second = parseInt(arr[2]);
  for (let i = 3; i < len; i++) {
    if (first <= parseInt(arr[i])) {
      second = first;
      first = parseInt(arr[i]);
      check = 0;
    } else if (check || second <= parseInt(arr[i])) {
      second = parseInt(arr[i]);
      check = 0;
    }
  }
  console.log(second);
}
