export const jobType = 'push_notification_code_3';

export function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobData in jobs) {
    const job = queue.create(jobType, jobData);
    job.on(
      'complete',
      () => console.log(`Notification job ${job.id} completed`)
    ).on(
      'failed',
      (error) => console.log(`Notification job ${job.id} failed: ${error}`)
    ).on(
      'progress',
      (progress) => console.log(`Notification job ${job.id} ${progress}% complete`)
    ).save((error) => {
      if (!error) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
  }
}
