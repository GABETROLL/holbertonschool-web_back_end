const chai = require('chai');
const chaiHttp = require('chai-http');

const app = require('./6-http_express');

chai.use(chaiHttp);
chai.should();

describe('Small HTTP server using Express', () => {
  it('Returns the right status', (done) => {
    chai.request(app)
      .get('/nope')
      .end((error, response) => {
        chai.expect(response.statusCode).to.equal(404);
        done();
      });
  });
});
