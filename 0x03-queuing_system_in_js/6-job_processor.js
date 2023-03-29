import { createQueue } from "kue";

const que = createQueue();
const que_name = 'push_notification_code'

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

que.process(que_name, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.messahe);
    done();
});