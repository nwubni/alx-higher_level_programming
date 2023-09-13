#!/usr/bin/node
const list = require('./100-data');
const res = list.map((x, index) => x * index);

console.log(JSON.stringify(list));
console.log(JSON.stringify(res));
