#!/usr/bin/node
/* prints the first argument passed to it
*/
let a;
if ((a = process.argv[2])) {
  console.log(a);
} else {
  console.log('No argument');
}
