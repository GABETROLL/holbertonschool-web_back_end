import { createPushNotificationsJobs, jobType } from "./8-job";
import kue from 'kue';
import chai from 'chai';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });

  const mockJobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
  ];

  it('display a error message if jobs is not an array', () => {
    chai.expect(() => createPushNotificationsJobs('not an array', queue))
      .to.throw(Error, 'Jobs is not an array');
  });
  it('create two new jobs to the queue', () => {
    createPushNotificationsJobs(mockJobs, queue);
    chai.expect(queue.testMode.jobs.length).to.equal(mockJobs.length);
  });
  it('creates jobs with type ``jobType`` and with same data as the `jobs` argument', () => {
    createPushNotificationsJobs(mockJobs, queue);
    for (const index in mockJobs) {
      const mockJob = mockJobs[index];
      const queueJob = queue.testMode.jobs[index];

      chai.expect(queueJob.type).to.equal(jobType);
      chai.expect(queueJob.data).to.eql(mockJob);
    }
  });
});
