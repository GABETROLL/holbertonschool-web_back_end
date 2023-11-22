const fsPromsises = require('fs/promises');

module.exports = function countStudents(path) {
  return fsPromsises.readFile(path, { encoding: 'utf8' })
    .then((data) => {
      // DATA SETUP:
      const splitData = data
        .split('\n')
        .map((row) => row.split(','));

      // The index of the header row in the CSV file,
      // assuming that the first non-empty row is the header,
      // and that the header has the field named: 'field'.
      const headerRowIndex = splitData.findIndex((row) => row.length);
      // The header row should have commas separating its fields,
      // since it's a CSV file.
      const columnNames = splitData[headerRowIndex];
      // The students are all of the following rows that are not empty.
      // They are stored as a JS object, with the column names as keys,
      // and the student's row's values as values.
      const students = splitData
        .slice(headerRowIndex + 1)
        .filter((row) => row.length === columnNames.length)
        .map((student) => {
          const result = {};

          for (const columnIndex in columnNames) {
            if (Object.hasOwn(columnNames, columnIndex)) {
              const column = columnNames[columnIndex];
              const studentColumnValue = student[columnIndex];
              result[column] = studentColumnValue;
            }
          }

          return result;
        });

      // LOG AMOUNT OF STUDENTS:
      console.log(`Number of students: ${students.length}`);

      // LOG THE AMOUNT OF STUDENTS AND THE STUDENTS FOR EACH FIELD:

      // A map of all of the fields that the students study,
      // and the list of the students that study it.
      const fields = new Map();
      for (const student of students) {
        if (fields.has(student.field)) {
          fields.get(student.field).push(student.firstname);
        } else {
          fields.set(student.field, [student.firstname]);
        }
      }

      fields.forEach((fieldStudents, field) => {
        console.log(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`);
      });
    })
    .catch(() => { throw new Error('Cannot load the database'); });
};
