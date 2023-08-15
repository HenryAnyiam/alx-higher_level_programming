#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const length = list.length;
  let i;
  for (i = 0; i < length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return (count);
};
