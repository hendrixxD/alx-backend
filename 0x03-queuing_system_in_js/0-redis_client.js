import { createClient } from "redis";

const client = createClient();

// client.on('error', err => console.log('Redis client not connected to the server: ', err));

if (client.connect()) {
    console.log('Redis client connected to the server');
} else {
    if (client.on('error', () => console.log('Redis client not connected to the server: ', err)));
};