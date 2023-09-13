#!/usr/bin/node
const parsedNumber = parseInt(process.argv[2]);

if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log('Not a number');
}
