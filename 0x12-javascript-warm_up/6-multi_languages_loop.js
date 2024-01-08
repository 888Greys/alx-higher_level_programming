#!/usr/bin/node
// script that prints 3 lines: (like 1-multi_languages.js
// but by using an array of string and a loop
const first = ['C is fun', 'Python is cool', 'Javascript is amazing'];

for (const f in first) {
  console.log(first[f]);
}
