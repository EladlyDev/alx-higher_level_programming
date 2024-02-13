#!/usr/bin/node

const fs = require('node:fs');
const args = require('node:process').argv;

if (args.length === 5) {
  const f1Data = fs.readFileSync(args[2], 'utf-8');
  const f2Data = fs.readFileSync(args[3], 'utf-8');
  const out = f1Data + f2Data;
  fs.writeFileSync(args[4], out);
}
