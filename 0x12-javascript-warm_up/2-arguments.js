#!/usr/bin/node
const count = process.argv.Length;
console.log(count === 2 ? 'No arguments' : count === 3 ? 'Arguments found' : 'Arguments found');
