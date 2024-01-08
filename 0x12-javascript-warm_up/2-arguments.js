#!/usr/bin/node
//  script that prints a message depending of the number of arguments passed:
const first = 'No argument';
const second = 'Argument found';
const third = 'Arguments found';

const numOfArgs = process.argv.length;

if (numOfArgs < 3) {
  console.log(first);
} else if (numOfArgs < 4) {
  console.log(second);
} else {
  console.log(third);
}
