import { createClient, print } from "redis";

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server: ' + err.message));
client.on('connect', () => console.log('Redis client connected to server'));

client.connect();

const key = 'HolbertonSchools';
const objs = {
    Portland: 50,
    Seattle: 80,
    Bogota: 20,
    'New York': 20,
    Cali: 40,
    Paris: 2,
};
 
function setNewSchool(schoolName, field, value) {
    client.hSet(schoolName, field, value, print);
}

async function displaySchoolValue(schoolName) {
    await client.hGetAll(schoolName, (_err, res) => {
        console.log(res);
    });
}

for (const[field, value] of Object.entries(objs)) {
    setNewSchool(key, field, value);
}

displaySchoolValue('HolbertonSchool');

// store the hash using hset
//client.hSet(key, value, print);

// display the hash using hgetall
//client.hGetAll(key, (err, value) => {
//    if (err) throw err(err);
//    console.log(value); // Should print the object with all key-value pairs
//});

// close the redis client
//client.disconnect();
