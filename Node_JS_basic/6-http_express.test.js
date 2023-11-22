const chai = require('chai');
const chaiHttp = require('chai-http');

const app = require('./6-http_express');

chai.use(chaiHttp);
chai.should();

describe('Small HTTP server using Express', () => {
  it('Returns the right content', (done) => {
    chai.request(app)
      .get('/')
      .end((error, response) => {
        chai.expect(response.text).to.equal('Hello Holberton School!');
        done();
      });
  });

  it('Returns the right status', (done) => {
    chai.request(app)
      .get('/')
      .end((error, response) => {
        chai.expect(response.statusCode).to.equal(200);
        done();
      });
  });
});
