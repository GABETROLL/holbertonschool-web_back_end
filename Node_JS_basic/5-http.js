const http = require('http');
const fs = require('fs');
const studentsTextOutput = require('./2-3-5-7-8-get_students_text');

const app = http.createServer((request, response) => {
  if (process.argv.length <= 1) {
    response.writeHead(500);
    response.end('Cannot load the database');
  } else if (request.url === '/') {
    response.writeHead(200);
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    const databaseFileName = process.argv[2];

    let data;
    try {
      data = fs.readFileSync(databaseFileName, 'utf8');
    } catch (error) {
      response.writeHead(500);
      response.end('Cannot load the database');
      return;
    }

    response.writeHead(200);
    const textOutput = studentsTextOutput(data).join('\n');
    response.end(`This is the list of our students\n${textOutput}`);
  } else {
    response.writeHead(404);
    response.end('Invalid URL');
  }
});
app.listen(1245);

module.exports = app;
