const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const chai = require('chai');

describe('sendPaymentRequestToApi', () => {
  let logSpy;

  beforeEach(() => {
    logSpy = sinon.spy(console, "log");
  });

  afterEach(() => {
    logSpy.restore();
  });

  it('logs: ``The total is: 120`` to the console, when being called with arguments: [100, 20]', () => {
    const args = [100, 20];
    sendPaymentRequestToApi(...args);

    const expectedTotal = args[0] + args[1];
    chai.expect(logSpy.calledOnce);
    chai.expect(logSpy.getCall(0).args).to.eql([`The total is: ${expectedTotal}`]);    
  });

  it('logs: ``The total is: 120`` to the console, when being called with arguments: [10, 10]', () => {
    const args = [10, 10];
    sendPaymentRequestToApi(...args);

    const expectedTotal = args[0] + args[1];
    chai.expect(logSpy.calledOnce);
    chai.expect(logSpy.getCall(0).args).to.eql([`The total is: ${expectedTotal}`]);
  });
});
