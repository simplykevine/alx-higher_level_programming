#!/usr/bin/node
const x = process.argv[2];
const str = 'C is fun';
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
}
