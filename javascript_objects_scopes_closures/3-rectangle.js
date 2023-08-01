#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }

print () {
    let i;
    let j;
    build = '';
    for (i = 0; i < this.height; i++) {
        if (i > 0) {
            build += '\n';
        }
        }
    console.log(build);
    } 
}

module.exports = Rectangle;
