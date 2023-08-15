#!/usr/bin/node
exports.addMeMaybe = function (a, b) {
  a++;
  b(a);
};
