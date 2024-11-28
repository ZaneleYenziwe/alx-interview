#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err || res.statusCode !== 200) {
    console.log('Failed to retrieve data');
    return;
  }

  const characters = body.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (err, res, characterBody) => {
      if (err || res.statusCode !== 200) {
        console.log('Failed to retrieve character data');
        return;
      }
      console.log(characterBody.name);
    });
  });
});

