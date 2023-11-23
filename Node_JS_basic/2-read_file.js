const fs = require('fs');
const studentsTextOutput = require('./2-3-5-7-8-get_students_text').studentsTextOutput;

module.exports = function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    console.error(err);
  }

  studentsTextOutput(data)
    .forEach((line) => console.log(line));
};
