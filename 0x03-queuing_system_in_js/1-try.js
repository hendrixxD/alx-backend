// import redis from 'redis';
import { createClient, print } from 'redis';

const client = createClient();

// client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));
// client.on('connect', () => console.log('Redis client connected to the server'));

if (client.connect()) {
    console.log('Redis client connected to the server');
} else {
    if (client.on('error', () => console.log('Redis client not connected to the server: ', err)));
};

// checks if redis client is open
if (client.isOpen) {
    console.log('Redis client is open\n');
} else {
    console.log('Redis client is not open\n');
}

// set a new key to a value
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

// get a value from a key
function displaySchoolValue(schoolName) {
  client.get(schoolName, (_err, value) => {
    if (_err) {
        console.log(_err);
    }
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
