const express = require('express');
const readFileSync = require('fs').readFileSync;
const studentsTextOutput = require('./2-3-5-7-8-get_students_text');

const databaseFileName = process.argv[2];

const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.get('/students', (request, response) => {
  const preamble = 'This is the list of our students\n';

  if (databaseFileName === undefined) {
    response.status(500);
    response.send(preamble + 'Cannot load the database');
    return;
  }

  let studentData;
  try {
    studentData = readFileSync(databaseFileName, 'utf8');
  } catch (error) {
    response.status(500);
    response.send(preamble + 'Cannot load the database');
    return;
  }

  response.send(preamble + studentsTextOutput(studentData).join('\n'));
  }
);
app.listen(1245);

module.exports = app;
