import { createQueue, Kue } from 'kue';

const que_name = 'push_notification_code';
const que = createQueue({name: que_name});

const job = que.create(que_name, {
    phoneNumber: '+234 ** ****',
    message: 'HendrixxSdiddy',
});

job
    .on('enqueue', (job, err) => {
        if (err) {
            console.log('Queueing failed', err);
        }
        console.log('Notification job created:', job.id);
    })
    .on('failed', () => {
        console.log('Notification job failed');
    })
    .on('completed', () => {
        console.log('Notification job completed');
    });

job.save();

