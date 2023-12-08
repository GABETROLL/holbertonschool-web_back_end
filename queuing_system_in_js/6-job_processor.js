import kue from 'kue';
const push_notification_code = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

push_notification_code.process('job', (notificationJob, done) => {
  sendNotification(
    notificationJob.data.phoneNumber,
    notificationJob.data.message
  );
  done();
});
