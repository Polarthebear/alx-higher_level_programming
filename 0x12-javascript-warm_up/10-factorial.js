#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative number is 1
  } else if (n === 0) {
    return 1; // Factorial of 0 is 1
  } else {
    return n * factorial(n - 1); // Recursive call to compute factorial
  }
}

const arg = parseInt(process.argv[2]);

console.log('The factorial of', arg, 'is:', factorial(arg));
