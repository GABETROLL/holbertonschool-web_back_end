/* eslint-disable */
import HolbertonCourse from './2-hbtn_course.js';
/* eslint-enable */

/*
Expected output in stdout:
--------------------------
HolbertonCourse {
  _name: 'ES6',
  _length: 1,
  _students: [ 'Bob', 'Jane' ]
}
ES6
1
[ 'Bob', 'Jane' ]
HolbertonCourse {
  _name: 'Python 101',
  _length: 3,
  _students: [ 'One', 'Two' ]
}
TypeError: Name must be a string.
TypeError: Length must be a number.
TypeError: Students must be an array of strings.
TypeError: Name must be a string.
TypeError: Length must be a number.
TypeError: Students must be an array of strings.
*/
let course1 = new HolbertonCourse('ES6', 1, ['Bob', 'Jane']);

console.log(course1);

console.log(course1.name);
console.log(course1.length);
console.log(course1.students);

course1.name = 'Python 101';
course1.length = 3;
course1.students = ['One', 'Two'];

console.log(course1);

try {
  course1.name = 12;
} catch (error) {
  console.log(error.toString());
}
try {
  course1.length = '4';
} catch (error) {
  console.log(error.toString());
}
try {
  course1.students = '["One", "Two"]';
} catch (error) {
  console.log(error.toString());
}

try {
  course1 = new HolbertonCourse({}, 5, ['Bob', 'Jane']);
} catch (error) {
  console.log(error.toString());
}
try {
  course1 = new HolbertonCourse('ES6', '1', ['Bob', 'Jane']);
} catch (error) {
  console.log(error.toString());
}
try {
  course1 = new HolbertonCourse('ES6', 3, undefined);
} catch (error) {
  console.log(error.toString());
}
