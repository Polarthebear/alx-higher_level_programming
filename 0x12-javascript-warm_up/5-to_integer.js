#!/usr/bin/node

const argc = process.argv.length;

if (argc > 2) {
  const number = parseInt(process.argv[2]);
  if (!isNaN(number)) {
    console.log('My number: ' + number);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
