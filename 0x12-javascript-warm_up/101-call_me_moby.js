#!/usr/bin/node
// Executes a function x times

exports.callMeMoby = function (x, theFunction) {
  for (let k = 0; k < x; k++) {
    theFunction();
  }
};
