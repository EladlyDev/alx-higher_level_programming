#!/usr/bin/node

const argv = process.argv;

if (argv.length > 3) {
  let i = 2;
  let biggest = parseInt(argv[i]);
  let sbiggest = parseInt(argv[++i]);
  let curr = parseInt(argv[i]);
  while (argv[i]) {
    curr = parseInt(argv[i]);
    if (curr > biggest) {
      sbiggest = biggest;
      biggest = curr;
    } else if (curr > sbiggest) { sbiggest = curr; }
    i++;
  }
  console.log(sbiggest);
} else { console.log(0); }
