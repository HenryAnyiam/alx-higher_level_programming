#!/usr/bin/node
exports.callMeMoby = function (a, b) {
  let i;
  for (i = 0; i < a; i++) {
    b();
  }
};
