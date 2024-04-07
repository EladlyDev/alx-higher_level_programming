#!/usr/bin/node
$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').append(data.hello);
  })});
