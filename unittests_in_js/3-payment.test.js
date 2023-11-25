const sinon = require('sinon');
let Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const chai = require('chai');

describe('sendPaymentRequestToApi', () => {
  it('uses ``Utils.calculateNumber`` to calculate the total', () => {
    Utils = sinon.spy(Utils);

    const args = [2, 4];
    sendPaymentRequestToApi(...args);

    chai.expect(Utils.calculateNumber.calledOnce).to.be.true;
    // DO NOT USE '.to.equal', THAT WILL FAIL.
    // USE '.to.eql', WHICH CHECKS IF THE ARRAY'S
    // CONTENTS ARE THE SAME, INSTEAD OF JS'
    // [...] === [...] or [...] == [...],
    // WHICH CHECKS IF THE ARRAYS ARE THE SAME
    // OBJECT, SINCE ARRAYS ARE OBJECTS,
    // AND OBJECTS ARE ONLY EQUAL IF THEY HAVE THE
    // SAME IDENTITY (ADDR).
    chai.expect(Utils.calculateNumber.getCall(0).args).to.eql(['SUM', ...args]);
  });
});
