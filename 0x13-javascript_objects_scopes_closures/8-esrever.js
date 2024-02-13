#!/usr/bin/node

exports.esrever = function (list) {
  const out = [];

  list.map((value, i, a) => { return out.unshift(value); });

  return out;
};
