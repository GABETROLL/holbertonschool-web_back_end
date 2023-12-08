import { createClient } from 'redis';

const client = createClient();
client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});
console.log('Redis client connected to the server');

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
client.subscribe('holberton school channel');
