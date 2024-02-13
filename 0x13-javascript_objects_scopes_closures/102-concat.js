#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

if (args.length === 5) {
  let out = fs.readFileSync(args[2], 'utf8');
  out += fs.readFileSync(args[3], 'utf8');
  fs.writeFileSync(args[4], out);
} else {
  console.log('Usage: sourcefile1 sourcefile2 destfile');
}
