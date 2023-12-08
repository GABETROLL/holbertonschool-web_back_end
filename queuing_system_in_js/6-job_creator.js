import kue from 'kue';

const jobObj = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

export const push_notification_code = kue.createQueue();
export const job = push_notification_code.create(
  'job',
  jobObj
).on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
}).save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});
