#!/usr/bin/node

let vec = [];

if (process.argv.length <= 3) {
    console.log(0);
}
else {
    for (let i = 2; i < process.argv.length; i++)
        vec.push(parseInt(process.argv[i]));

    vec = vec.sort();

    console.log(vec[vec.length - 2]);
}