#!/usr/bin/node

const argv = process.argv;
let size = parseInt(argv[2]);
const out = (size >= 0) ? 'X'.repeat(size) : '';

if (size) {
  while (size > 0) {
    console.log(out);
    size--;
  }
} else { console.log('Missing size'); }
