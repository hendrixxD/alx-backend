import { createClient } from "redis";

const client = createClient();

client.connect();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log("Redis client connected to the server"));

const channel = "holberton school channel";

function publishMessage(message, time) {
    setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish(channel, message);
    }, time);
};

client.on('message', (_err, msg) => {
    if (message === EXIT_MSG) {
        subscriber.unsubscribe();
        subscriber.quit();
        process.exit(0);
    }
    console.log(message);
});

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
