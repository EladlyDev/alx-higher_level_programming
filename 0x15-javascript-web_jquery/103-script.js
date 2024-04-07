#!/usr/bin/node
$(document).ready(() => {
  const fetch = () => {
    const lang = $('INPUT#language_code').val()
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, data => {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').on('click', fetch);
  $('INPUT#language_code').keypress((e) => {
    if (e.which == 13) { fetch();}
  });
});
