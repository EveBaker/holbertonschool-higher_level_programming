#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const urlEndpoint = `https://swapi-api.hbtn.io/api/films/${movieID}`;

request(urlEndpoint, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode !== 200) {
    console.error('Error:', body);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});