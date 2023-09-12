#!/usr/bin/node

function add(a, b) {
    const x = parseInt(a);
    const y = parseInt(b);

    console.log(x + y);
}

add(process.argv[2], process.argv[3]);