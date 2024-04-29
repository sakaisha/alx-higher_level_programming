#!/usr/bin/node
/* prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
let value;
let num;
if ((value = process.argv[2]) && (num = parseInt(value))) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
