import { createClient, print } from "redis";

const client = createClient();
const EXIT_MSG = 'KILL_SERVER';

client.connect();

// subscriber = client.duplicate();
// subscriber.connect();
// subscriber.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
// subscriber.on('connect', () => console.log("Redis client connected to the server"));

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log("Redis client connected to the server"));

const channel = "holberton school channel";

client.subscribe(channel);

client.on('message', (_err, msg) => {
    if (message === EXIT_MSG) {
        subscriber.unsubscribe();
        subscriber.quit();
        process.exit(0);
    }
    console.log(message);
});
