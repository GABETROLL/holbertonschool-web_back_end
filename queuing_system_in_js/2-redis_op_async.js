import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', error => {
  console.log(`Redis client not connected to the server: ${error}`);
});
console.log('Redis client connected to the server');

client.get = promisify(client.get);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  console.log(await client.get(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
