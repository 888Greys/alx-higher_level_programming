#!/usr/bin/node
// script that prints the first argument passed to it
const first = 'No argument';

console.log(process.argv[2] || first);
