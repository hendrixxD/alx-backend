import { createClient, print } from "redis";

// connect to redis client
const client = createClient();
client.connect();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

// checks if redis client is open
if (client.isOpen) {
    console.log('Redis client is open');
} else {
    console.log('Redis client is not open');
}

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (_err, val) => {
        if (_err) {
            console.log(_err);
        }
        console.log(val);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');