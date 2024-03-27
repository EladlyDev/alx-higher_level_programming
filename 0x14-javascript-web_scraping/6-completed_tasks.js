#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const url = argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const tasks = JSON.parse(body);
    const completed = {};

    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        if (tasks[i].userId in completed) { completed[tasks[i].userId]++; } else { completed[tasks[i].userId] = 1; }
      }
    }
    console.log(completed);
  }
});
