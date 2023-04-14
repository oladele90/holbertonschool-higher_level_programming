#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
}).pipe(fs.createWriteStream(process.argv[3]));
