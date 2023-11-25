const request = require('request');
const chai = require('chai');

describe('index page', () => {
  it('responds with ``Welcome to the payment system``, when requested with ``GET /``', (done) => {
    request('http://localhost:7865/', (error, response, body) => {
      if (error) {
        done(error);
      } else {
        try{
          chai.expect(body).to.equal('Welcome to the payment system');
          done();
        } catch (error) {
          done(error);
        }
      }
    });
  });
});
