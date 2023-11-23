const express = require('express');

const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.get('/students', (request, response) => {
  response.send('This is the list of our students\n');
});
app.listen(1245);

module.exports = app;
