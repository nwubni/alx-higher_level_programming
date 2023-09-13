#!/usr/bin/node

function factorial (x) {
  if (x === undefined || x === null || x <= 1) { return 1; }

  return (x * factorial(x - 1));
}

const ans = factorial(process.argv[2]);
console.log(ans);
