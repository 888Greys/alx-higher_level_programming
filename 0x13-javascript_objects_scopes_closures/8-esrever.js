#!/usr/bin/node
/*
 * a function that returns the reversed version of a list:
 */

exports.esrever = function (list) {
  const rev = [];
  const size = list.length - 1;

  for (const i in list) {
    rev[i] = list[size - i];
  }
  return rev;
};
