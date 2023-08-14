#!/usr/bin/node
const { argv } = require('process');
let a;
a = Number(argv[2]);
if (isNaN(a)) {
  a = 0;
}
function factorial (a) {
  if (a == 0 || a == 1) {
	return (1);
}
  return (a + factorial(a - 1));
}
console.log(factorial(a));
