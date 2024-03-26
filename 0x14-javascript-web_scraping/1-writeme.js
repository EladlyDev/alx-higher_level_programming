#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

const fname = argv[2];
const data = argv[3];

fs.writeFile(fname, data, err => {
  if (err) {
    console.log(err);
  }
});
