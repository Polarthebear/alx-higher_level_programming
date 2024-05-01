#!/usr/bin/node
/**
 * Class that represents a rectangle
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * if w or h = 0 or not +ve int, create empty object
 * Create an instance method called print() that prints the rectangle using the character X
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
	  for (let i = 0; i < this.height; i++) {
		  let space = '';
		  let y = 0;
		  while (y < this.width) {
			  space += 'X';
			  y++;
		  }

		  console.log(space);
	  }
  }
}
module.exports = Rectangle;
