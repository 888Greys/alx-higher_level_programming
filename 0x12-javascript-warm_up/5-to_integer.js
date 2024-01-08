#!/usr/bin/node
// script that prints My number: <first argument converted in
// integer> if the first argument can be converted to an integer:
const first = 'Not a number';

const arg = process.argv[2];

if (isNaN(parseInt(+arg))) {
  console.log(first);
} else {
  console.log('My number: ' + parseInt(+arg));
}
