const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  // 2D matrix of the CSV data
  // If a line in the file was empty,
  // the row is ``[]``.
  const table = data
    .split('\n')
    .map((row) => row.split(','));

  // index of first row in 'table' that's not empty
  const tableHeadIndex = table.findIndex((row) => row.length);
  // 1D matrix of the names of all of the columns in the CSV file
  const tableHead = table[tableHeadIndex];
  // the amount of values each (student) row must have,
  // as decided from the first row, which is believed to be the header row,
  // and is believed to be the one described above.
  const validRowLength = tableHead.length;

  // 2D matrix of all of the (student) rows in 'table'
  // that have the same length as ``tableHead``,
  // since we're considering those invalid.
  const tableBody = table
    .slice(tableHeadIndex + 1)
    .filter((row) => row.length === validRowLength);

  // The fields we assume the students CSV file has
  const firstnameIndex = tableHead.indexOf('firstname');
  const fieldIndex = tableHead.indexOf('field');

  const result = {};

  // result should now be an object
  // with the 'field' values in each row as its keys,
  // and [] as its values
  for (const row of tableBody) {
    result[row[fieldIndex]] = [];
  }

  // ``result`` should now be an object
  // with the 'field' values in each row as its keys,
  // and the 'firstname' of each (student) row that studies
  // that 'field'.
  for (const row of tableBody) {
    result[row[fieldIndex]].push(row[firstnameIndex]);
  }

  // OUTPUT TEXT
  let output = `Number of students: ${tableBody.length}`;
  console.log(output);

  for (const [field, fieldStudents] of Object.entries(result)) {
    output = `Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`;
    console.log(output);
  }
}

module.exports = countStudents;
