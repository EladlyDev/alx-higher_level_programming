#!/usr/bin/node

exports.nbOccurences = function (list, se) {
  let occ = 0;

  for (let i = 0; i < list.length; i++) { occ += list[i] === se ? 1 : 0; }

  return occ;
};
