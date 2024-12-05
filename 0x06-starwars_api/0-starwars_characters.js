#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL for the Star Wars API films endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch the movie details
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch movie details (Status code: ${response.statusCode})`);
    return;
  }

  const data = JSON.parse(body);

  // Retrieve the list of character URLs
  const characters = data.characters;

  // Fetch and display character names in order
  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
        return;
      }

      if (charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      }
    });
  });
});
