#!/usr/bin/node

const argv = require('node:process').argv;
const arglen = argv.length;

if (arglen < 3) {
  console.log('No argument');
} else if (arglen === 3) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
