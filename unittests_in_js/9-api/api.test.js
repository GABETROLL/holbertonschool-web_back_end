const request = require('request');
const chai = require('chai');

describe('index page', () => {
  it('responds with ``Welcome to the payment system``, when requested with ``GET /``,\
 at ``http://localhost:7865``', (done) => {
    request('http://localhost:7865/', (error, response, body) => {
      if (error) {
        done(error);
      } else {
        try{
          chai.expect(response.statusCode).to.equal(200);
          chai.expect(body).to.equal('Welcome to the payment system');
          done();
        } catch (error) {
          done(error);
        }
      }
    });
  });
});

describe('cart page', () => {
  it('responds with ``Payment methods for cart :id``,\
 when requested with ``GET /cart/:id``\
 at ``http://localhost:7865``,\
 and ``id`` is a valid representation of an integer in base 10', (done) => {
    const testId = 10;
  
    request(`http://localhost:7865/cart/${testId}`, (error, response, body) => {
      if (error) {
        done(error);
      } else {
        try {
          chai.expect(response.statusCode).to.equal(200);
          chai.expect(body).to.equal(`Payment methods for cart ${testId}`);
          done();
        } catch (error) {
          done(error);
        }
      }
    });
  });

  it('responds with an error code of ``404``,\
 when the ``id`` is not a valid base 10 integer string representation', (done) => {
    const testInvalidId = '98-HHHH5';

    request(`http://localhost:7865/cart/${testInvalidId}`, (error, response, body) => {
      if (error) {
        done(error);
      } else {
        try {
          chai.expect(response.statusCode).to.equal(404);
          chai.expect(body).to.equal(`<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /cart/${testInvalidId}</pre>
</body>
</html>
`);
          done();
        } catch (error) {
          done(error);
        }
      }
    });
  });
});
