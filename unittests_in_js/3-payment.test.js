const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const chai = require('chai');

describe('sendPaymentRequestToApi', () => {
  it('uses ``Utils.calculateNumber`` to calculate the total', () => {
    const sandbox = sinon.createSandbox();
    sinon.spy(Utils.calculateNumber);

    const args = [2, 4];
    sendPaymentRequestToApi(...args);

    chai.expect(Utils.calculateNumber.calledOnce()).to.be.true;
    chai.expect(Utils.calculateNumber.getCall(0).args).to.equal(args);

    sandbox.restore();
  });
});
