const http = require('http');

const app = http.createServer((request, response) => {
  response.writeHead(200);
  response.end('Hello Holberton School!');
});
app.listen(1245, 'localhost');

module.exports = app;
