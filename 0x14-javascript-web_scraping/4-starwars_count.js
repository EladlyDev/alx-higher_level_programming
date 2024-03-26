#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

const url = argv[2];

request(url, (err, res, body) => {
  if (!err) {
    let out = 0;
    JSON.parse(body).results.forEach(film => {
      film.characters.forEach(char => {
        if (char.includes('18')) { out++; }
      });
    });
    console.log(out);
  }
});
