#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const r = JSON.parse(body)
    let count = 0
    for(let i = 0; i < r.count; i++) {
        if (r.results[i].characters.includes("https://swapi-api.hbtn.io/api/people/18/")) {
            count++
        }
    }
    console.log(count)
}
});
