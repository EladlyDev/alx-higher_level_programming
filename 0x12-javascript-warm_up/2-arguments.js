#!/usr/bin/node

const arglen = process.argv.length;

if (arglen > 3) {
  console.log('Arguments found');
} else if (arglen === 3) {
  console.log('Argument found');
} else { console.log('No argument'); }
