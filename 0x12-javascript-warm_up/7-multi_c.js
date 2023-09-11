#!/usr/bin/node
// Prints x times 'C is fun'

const args = process.argv;
const num = parseInt(args[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let k = 0; k < args[2]; k++) {
    console.log('C is fun');
  }
}
