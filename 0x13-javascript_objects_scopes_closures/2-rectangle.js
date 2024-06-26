#!/usr/bin/node
/**
 * Class that represents a rectangle
 * The constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * if w or h = 0 or not +ve int, create empty object
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
