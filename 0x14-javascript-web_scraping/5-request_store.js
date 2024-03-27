#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');
const fs = require('fs');

const url = argv[2];
const fName = argv[3];

request.get(url).pipe(fs.createWriteStream(fName));
