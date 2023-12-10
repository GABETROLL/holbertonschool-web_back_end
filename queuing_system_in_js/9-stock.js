import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
  {itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
  {itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
  {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5}
];
function getItemById(id) {
  return listProducts[id - 1];
}

const app = express();
app.get('/list_products', (request, response) => {
  response.send(JSON.stringify(listProducts));
});

const redisClient = redis.createClient();
function reserveStockById(itemId, stock) {
  // assuming there's enough stock,
  // and that `itemId` is valid.
  const item = getItemById(itemId);

  if (item.currentQuantity === undefined) {
    item.currentQuantity = item.initialAvailableQuantity;
  }
  item.currentQuantity -= stock;

  redisClient.set(`item.${itemId}`, JSON.stringify(item));
}
async function getCurrentReservedStockById(itemId) {
  redisClient.get = promisify(redisClient.get);
  return await redisClient.get(`item.${itemId}`);
}

// ?
app.get('/list_products/:itemId', (request, response) => {
  getCurrentReservedStockById(request.params.itemId)
    .then((item) => {
      if (!item) {
        response.status(404);
        response.send({ 'status': 'Product not found' });
      } else {
        response.send(JSON.parse(item));
      }
    });
});
app.get('/reserve_product/:itemId', (request, response) => {
  const item = getItemById(request.params.itemId);

  if (item === undefined) {
    response.status(404);
    response.send({ 'status': 'Product not found' });
    return;
  }
  if (item.currentQuantity < 1) {
    response.status(403);
    response.send({ 'status': 'Not enough stock available', 'itemId': item.itemId });
    return;
  }
  reserveStockById(item.itemId, 1);
  response.status(200);
  response.send({'status': 'Reservation confirmed', 'itemId': item.itemId });
});
app.listen(1245);
