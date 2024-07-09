#!/usr/bin/node
/* eslint-disable quotes */

const { argv } = require("node:process");

function add (a, b) {
  return a + b;
}

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log(`NaN`);
} else {
  console.log(add(a, b));
}
