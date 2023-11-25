const getPaymentTokenFromAPI = require('./6-payment_token');
const chai = require('chai');

describe('getPaymentTokenFromAPI', () => {
  it('returns a resolved promise when called with true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((data) => {
        try{
          chai.expect(data).to.eql({ data: 'Successful response from the API' });
          done();
        } catch (error) {
          done(error);
        }
      });
  });
  it('does nothing when not called with true', () => {
    chai.expect(
      getPaymentTokenFromAPI(false)
    ).to.equal(undefined);

    chai.expect(
      getPaymentTokenFromAPI()
    ).to.equal(undefined);
  });
});
