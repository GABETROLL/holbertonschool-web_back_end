import { createClient, print } from 'redis';

const client = createClient();
client.on('error', error => {
  console.log(`Redis client not connected to the server: ${error}`);
});
console.log('Redis client connected to the server');

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, replies) => console.log(replies));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
