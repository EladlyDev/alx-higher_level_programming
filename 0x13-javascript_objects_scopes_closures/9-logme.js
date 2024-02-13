#!/usr/bin/node

class Log {
  constructor (item) {
    if (!Log.occ) Log.occ = 0;
    console.log(`${Log.occ}: ${item}`);
    Log.occ++;
  }
}

exports.logMe = function (item) {
  return new Log(item);
};
