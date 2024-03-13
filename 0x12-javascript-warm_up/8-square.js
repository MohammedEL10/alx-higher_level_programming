#!/usr/bin/node
// print a square

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for ( i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.pepeat(parseInt(process.argv[2])));
  }
}
