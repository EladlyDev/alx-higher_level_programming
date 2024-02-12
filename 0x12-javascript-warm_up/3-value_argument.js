#!/usr/bin/node

const argv = require('node:process').argv;

if (!argv[2]) {
  console.log('No argument');
} else if (argv[2]) {
  console.log(argv[2]);
}
