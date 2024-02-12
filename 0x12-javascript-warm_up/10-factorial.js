#!/usr/bin/node

const argv = process.argv;
const no = parseInt(argv[2]);

function factorial (no) {
  if (!no) { return 1; }

  return no * factorial(no - 1);
}

console.log(factorial(no));
