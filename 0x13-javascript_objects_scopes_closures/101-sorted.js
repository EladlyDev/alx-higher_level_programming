#!/usr/bin/node

const dict = require('./101-data.js').dict;

const out = {};

Object.keys(dict).forEach((key) => {
  const value = dict[key];
  if (!out[value]) {
    out[value] = [key];
  } else {
    out[value].push(key);
  }
});

console.log(out);
