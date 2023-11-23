const fs = require('fs');

function studentsTextOutput(data) {
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
  // They are stored an Array of student objects,
  // with the column names as keys,
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

  // TEXT OUTPUT SETUP:
  const result = [`Number of students: ${students.length}`];
  fields.forEach((fieldStudents, field) =>
    result.push(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`)
  );

  return result;
}

module.exports = studentsTextOutput;
