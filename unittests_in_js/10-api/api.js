const express = require('express');

const port = 7865;
const app = express();
app.get('/', (request, response) => {
  response.send('Welcome to the payment system');
});
app.get('/cart/:id([0-9]+)', (request, response) => {
  const { id } = request.params;
  const idInt = parseInt(id, 10);
  response.send(`Payment methods for cart ${idInt}`);
});
app.get('/available_payments', (request, response) => {
  response.send({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    }
  });
});
app.post('/login/', (request, response) => {
  const userName = request.body;
  response.send(`Welcome ${userName}`);
});
app.listen(port, () => console.log(`API available on localhost port ${port}`));
