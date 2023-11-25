const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const chai = require('chai');

describe('sendPaymentRequestToApi', () => {
  it('uses ``Utils.calculateNumber`` to calculate the total', () => {
    Utils.calculateNumber = sinon.spy(Utils.calculateNumber);

    const args = [2, 4];
    sendPaymentRequestToApi(...args);

    chai.expect(Utils.calculateNumber.calledOnce()).to.be.true;
    chai.expect(Utils.calculateNumber.getCall(0).args).to.equal(args);

    Utils.calculateNumber.restore();
  });
});
