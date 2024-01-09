#!/usr/bin/node
const dict = require('./101-data').dict; const newDict = {};
for (const userId in dict) newDict[dict[userId]] ? newDict[dict[userId]].push(userId) : newDict[dict[userId]] = [userId];
console.log(newDict);
