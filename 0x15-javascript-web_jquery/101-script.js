#!/usr/bin/node
$(document).ready(() => {
  const list = $('UL.my_list')
  $('DIV#add_item').on('click', () => {
    list.append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', () => {
    $('UL.my_list :last-child').remove()
  });
  $('DIV#clear_list').on('click', () => {
    list.empty()
  });
});
