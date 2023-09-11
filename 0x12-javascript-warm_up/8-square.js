#!/usr/bin/node
// Prnts a square of a specified size

const args = process.argv;
const size = parseInt(args[2], 10);
const row = [];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let k = 0; k < size; k++) {
    row.push('X');
  }
  for (let k = 0; k < size; k++) {
    console.log(row.join(''));
  }
}
