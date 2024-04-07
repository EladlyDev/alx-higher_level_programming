#!/usr/bin/node
$.get('https://swapi-api.alx-tools.com/api/films/?format=json',
  data => {
    for (const i in data.results) {
      $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
    }
  });
