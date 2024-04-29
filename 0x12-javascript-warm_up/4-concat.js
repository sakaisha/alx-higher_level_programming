#!/usr/bin/node
/* prints two arguments passed to it, in the following format
*/
let sentence = '';
if (process.argv[3]) {
  sentence = process.argv[2] + ' is ' + process.argv[3];
} else if (process.argv[2]) {
  sentence = process.argv[2] + ' is undefined';
} else {
  sentence = 'undefined is undefined';
}
console.log(sentence);
