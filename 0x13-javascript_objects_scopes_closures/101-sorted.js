#!/usr/bin/node
const dict = require('./101-data.js').dict;
const res = new Map();

for (const key in dict) {
  if (!res.has(dict[key])) {
    res.set(dict[key], []);
  }

  res.get(dict[key]).push(key);
}

console.log(Object.fromEntries(res));
