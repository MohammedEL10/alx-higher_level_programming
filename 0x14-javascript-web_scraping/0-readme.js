#!/usr/bin/node
import { readFileSync } from 'node:fs';
const fs = require("fs");


fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
