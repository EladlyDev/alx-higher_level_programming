#!/usr/bin/node

const argv = process.argv;
const no1 = parseInt(argv[2]);
const no2 = parseInt(argv[3]);

function add (a, b) { return a + b; }

console.log(add(no1, no2));
