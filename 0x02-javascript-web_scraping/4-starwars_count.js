#!/usr/bin/node
const request = require('request');
const Wedge = 'https://swapi-api.hbtn.io/api/people/18/';
request(process.argv[2], function (error, response, body) {
  if (error) {
    throw error;
  } else {
    const result = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < result.length; i++) {
      if (result[i].characters.includes(Wedge)) {
        count++;
      }
    }
    console.log(count);
  }
});
