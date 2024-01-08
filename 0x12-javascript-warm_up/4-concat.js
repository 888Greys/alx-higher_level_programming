#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: “ is ”
const first = 'undefined';

console.log((process.argv[2] || first) + ' is ' + (process.argv[3] || first));
