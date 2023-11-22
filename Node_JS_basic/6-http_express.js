const express = require('express');

const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.listen(1245);

module.exports = app;
