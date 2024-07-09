#!/usr/bin/env node
/* eslint-disable quotes */

const { argv } = require("node:process");

const size = parseInt(argv[2]);
if (isNaN(size)) {
  console.log(`Missing size`);
} else {
  for (let i = 0; i < size; i++) {
    console.log(`X`.repeat(size));
  }
}
