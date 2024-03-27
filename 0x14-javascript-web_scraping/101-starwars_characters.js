#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

request(url, async (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const body = await new Promise((resolve, reject) => {
        request(character, (err, res, body) => {
          if (err) reject(err);
          else resolve(body);
        });
      });
      console.log(JSON.parse(body).name);
    }
  }
});
