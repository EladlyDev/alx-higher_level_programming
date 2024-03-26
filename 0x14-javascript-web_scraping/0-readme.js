#!/usr/bin/node
const argv = require('process').argv;
const fs = require('fs');

const fname = argv[2];

fs.readFile(fname, (err, data) => {
  if (err) {
    console.log(err);
  } else { console.log(data.toString()); }
});
