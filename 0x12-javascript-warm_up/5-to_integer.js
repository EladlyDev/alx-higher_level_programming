#!/usr/bin/node

const argv = process.argv;
const no = parseInt(argv[2]);

if (no)
{
    console.log('My number: ' + no);
} else { console.log('Not a number'); }
