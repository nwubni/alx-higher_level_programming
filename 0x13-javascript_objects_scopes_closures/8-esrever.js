#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let t;

  for (let i = 0; i < len; i++) {
    t = list[i];
    list[i] = list[len];
    list[len] = t;
    len--;
  }

  return list;
};
