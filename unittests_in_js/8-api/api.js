const express = require('express');

const app = express();
app.get('/', (request, response) => {
  response.send('Welcome to the payment system');
});
app.listen(7865, () => console.log('API available on localhost port 7865'));
