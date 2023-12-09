import kue from 'kue';

const blacklistedPhoneNumbers = [
  '4153518780',
  '4153518781'
];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistedPhoneNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const push_notification_code_2 = kue.createQueue();
push_notification_code_2.process('second job', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
