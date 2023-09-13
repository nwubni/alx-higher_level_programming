#!/usr/bin/node

const vec = [];

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) { vec.push(parseInt(process.argv[i])); }

  vec.sort((a, b) => a - b);

  console.log(vec[vec.length - 2]);
}
