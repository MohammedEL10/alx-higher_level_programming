#!/usr/bin/node
const count = process.argv.Length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
