const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const chai = require('chai');

describe('sendPaymentRequestToApi', () => {
  it('uses ``Utils.calculateNumber`` to calculate the total', () => {
    const calculateNumberFakeResult = 10;

    // THESE ARE APIS FOR THE METHODS,
    // NOT THE OBJECTS.
    // ``logSpy`` IS NOT AN IMPOSTOR FOR 'console',
    // IT'S AN IMPOSTOR FOR 'console.log'.
    // SAME TRUTH APPLIES TO ``calculateNumberStub``.
    const calculateNumberStub = sinon.stub(Utils, "calculateNumber")
      .callsFake(() => calculateNumberFakeResult);
    const logSpy = sinon.spy(console, "log");

    const args = [100, 20];
    sendPaymentRequestToApi(...args);

    chai.expect(calculateNumberStub.calledOnce).to.be.true;
    // DO NOT USE '.to.equal', THAT WILL FAIL.
    // USE '.to.eql', WHICH CHECKS IF THE ARRAY'S
    // CONTENTS ARE THE SAME, INSTEAD OF JS'
    // [...] === [...] or [...] == [...],
    // WHICH CHECKS IF THE ARRAYS ARE THE SAME
    // OBJECT, SINCE ARRAYS ARE OBJECTS,
    // AND OBJECTS ARE ONLY EQUAL IF THEY HAVE THE
    // SAME IDENTITY (ADDR).
    chai.expect(calculateNumberStub.getCall(0).args).to.eql(['SUM', ...args]);

    chai.expect(logSpy.calledOnce);
    chai.expect(logSpy.getCall(0).args).to.eql([`The total is: ${calculateNumberFakeResult}`]);

    calculateNumberStub.restore();
    logSpy.restore();
  });
});
