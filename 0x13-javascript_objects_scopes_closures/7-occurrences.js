#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (const element of list) { count += element === searchElement; }

  return count;
};
