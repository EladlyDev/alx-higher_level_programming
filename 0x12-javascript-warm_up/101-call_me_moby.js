#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  if (theFunction) {
    while (x) {
      theFunction();
      x--;
    }
  }
};
