#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

request(url, function (error, response, body) {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch the movie. Status code:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, function (charError, charResponse, charBody) {
      if (charError) {
        console.error('Error fetching character:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character. Status code:', charResponse.statusCode);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
