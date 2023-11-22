const http = require('http');
const countStudents = require('./3-read_file_async.js');

const app = http.createServer((request, response) => {
  response.writeHead(200);
  response.end(request.url === '/'
    ? 'Hello Holberton School!'
    : ''
  );
});
app.listen(1245);

module.exports = app;
