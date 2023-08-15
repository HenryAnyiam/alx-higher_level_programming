#!/usr/bin/node
exports.esrever = function (list) {
  const length = list.length - 1;
  let myLength = list.length - 1;
  const myArray = [];
  let i;
  for (i = 0; i <= length; i++) {
    myArray[i] = list[myLength];
    myLength--;
  }
  return (myArray);
};
