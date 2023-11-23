/* eslint-disable import/no-unresolved */
const fsPromsises = require('fs/promises');
const studentsTextOutput = require('./2-3-5-7-8-get_students_text');

module.exports = function countStudents(path) {
  return fsPromsises.readFile(path, { encoding: 'utf8' })
    .then((data) => {
      studentsTextOutput(data)
        .forEach((line) => console.log(line));
    })
    .catch(() => { throw new Error('Error: Cannot load the database'); });
};
