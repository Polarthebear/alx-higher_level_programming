#!/usr/bin/node

const args = process.argv.length - 2; // Subtracting 2 for the executable path and script filename

if (args === 1) {
  console.log('Argument Found');
} else if (args === 0) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
