import { createClient } from 'redis';

const client = createClient()
  .on('error', error => console.log(`Redis client not connected to the server: ${error}`))
  .connect();
console.log('Redis client connected to the server');
