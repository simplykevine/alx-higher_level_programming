#!/usr/bin/node
const srcA = process.argv[2];
const srcB = process.argv[3];
const dest = process.argv[4];
const fs = require('fs');
const srcTextA = fs.readFileSync(srcA);
const srcTextB = fs.readFileSync(srcB);
fs.writeFileSync(dest, srcTextA + srcTextB);
