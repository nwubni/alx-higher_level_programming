#!/usr/bin/node

const size = parseInt(process.argv[2]);
let output = '';

if (process.argv.length === 2) {
    console.log("Missing size");
}
else if (!isNaN(size)) {
    for (let i = 1; i <= size; i++) {
        for (let j = 1; j <= size; j++) {
            output += 'X';
        }

        console.log(output);
        output = '';
    }
} else {
    console.log("Missing size");
}