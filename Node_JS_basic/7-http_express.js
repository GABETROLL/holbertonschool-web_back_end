const express = require('express');
const readFileSync = require('fs').readFileSync;
const studentsTextOutput = require('./2-3-5-7-8-get_students_text');

const databaseFileName = process.argv[2];

const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.get('/students', (request, response) => {
  if (databaseFileName === undefined) {
    response.status(500);
    response.send('Internal server error');
  }

  let studentData;
  try {
    studentData = readFileSync(databaseFileName, 'utf8');
  } catch (error) {
    response.status(500);
    response.send('Internal server error');
  }

  const textOutput = studentsTextOutput(studentData).join('\n');
  response.send(`This is the list of our students\n${textOutput}`);
});
app.listen(1245);

module.exports = app;
