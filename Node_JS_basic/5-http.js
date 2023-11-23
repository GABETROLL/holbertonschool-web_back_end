const http = require('http');
const get_students_text = require('./2-3-5-7-8-get_students_text');
const safeReadFileSync = get_students_text.safeReadFileSync;
const studentsTextOutput = get_students_text.studentsTextOutput;

const app = http.createServer((request, response) => {
  if (process.argv.length <= 1) {
    response.writeHead(500);
    response.end('Internal server error');
  } else if (request.url === '/') {
    response.writeHead(200);
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    const databaseFileName = process.argv[2];
    const data = safeReadFileSync(databaseFileName);
    if (data === undefined) {
      response.writeHead(500);
      response.end('Internal server error');
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
