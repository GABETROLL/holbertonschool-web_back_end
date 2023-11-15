import HolbertonCourse from "./2-hbtn_course.js";

/*
Expected output in stdout:
HolbertonCourse { "ES6", 1, ["Bob", "Jane"] }
HolbertonCourse { "Python 101", 3, ["One", "Two"] }
TypeError: `name` must be a string.
TypeError: `length` must be a number.
TypeError: `students` must be an array of strings.
TypeError: `name` must be a string.
TypeError: `length` must be a number.
TypeError: `students` must be an array of strings.
*/
const course1 = new HolbertonCourse("ES6", 1, ["Bob", "Jane"]);

console.log(course1);

course1.name = "Python 101";
course1.length = 3;
course1.students = ["One", "Two"];

console.log(course1);

try {
  course1.name = 12;
} 
catch(error) {
  console.log(error.toString());
}
try {
  course1.length = "4";
}
catch(error) {
  console.log(error.toString());
}
try {
  course1.students = '["One", "Two"]';
}
catch(error) {
  console.log(error.toString());
}

try {
  const course2 = new HolbertonCourse({}, 5, ["Bob", "Jane"]);
}
catch(error) {
  console.log(error.toString());
}
try {
  const course2 = new HolbertonCourse("ES6", "1", ["Bob", "Jane"]);
}
catch(error) {
  console.log(error.toString());
}
try {
  const course2 = new HolbertonCourse("ES6", 3, undefined);
}
catch(error) {
  console.log(error.toString());
}
