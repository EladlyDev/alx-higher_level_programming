#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

const url = argv[2];

request.get(url).on('response', res => {
  console.log('code:', res.statusCode);
});
