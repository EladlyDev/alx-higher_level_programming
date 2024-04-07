#!/usr/bin/node
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  $('#hello').append(data.hello);
});
