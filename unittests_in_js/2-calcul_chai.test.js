const calculateNumber = require('./2-calcul_chai');
const chai = require('chai');

describe('calculateNumber', () => {
  it('sums rounded ``a`` and rounded ``b``, as ``Math.floor`` rounds', () => {
    chai.expect(calculateNumber('SUM', 0, 0)).to.equal(0);

    chai.expect(calculateNumber('SUM', 0.25, 0)).to.equal(0);
    chai.expect(calculateNumber('SUM', 0, 0.25)).to.equal(0);
    chai.expect(calculateNumber('SUM', 0.25, 0.25)).to.equal(0);

    chai.expect(calculateNumber('SUM', -0.25, 0)).to.equal(0);
    chai.expect(calculateNumber('SUM', 0, -0.25)).to.equal(0);
    chai.expect(calculateNumber('SUM', -0.25, -0.25)).to.equal(0);

    chai.expect(calculateNumber('SUM', 0.5, 0)).to.equal(1);
    chai.expect(calculateNumber('SUM', 0, 0.5)).to.equal(1);
    chai.expect(calculateNumber('SUM', 0.5, 0.5)).to.equal(2);
    
    chai.expect(calculateNumber('SUM', -0.5, 0)).to.equal(0);
    chai.expect(calculateNumber('SUM', 0, -0.5)).to.equal(0);
    chai.expect(calculateNumber('SUM', -0.5, -0.5)).to.equal(0);
  });
  it('subtracts rounded ``b`` from rounded ``a``, as ``Math.floor`` rounds', () => {
    chai.expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);

    chai.expect(calculateNumber('SUBTRACT', 0.25, 0)).to.equal(0);
    chai.expect(calculateNumber('SUBTRACT', 0, 0.25)).to.equal(0);
    chai.expect(calculateNumber('SUBTRACT', 0.25, 0.25)).to.equal(0);

    chai.expect(calculateNumber('SUBTRACT', -0.25, 0)).to.equal(0);
    chai.expect(calculateNumber('SUBTRACT', 0, -0.25)).to.equal(0);
    chai.expect(calculateNumber('SUBTRACT', -0.25, -0.25)).to.equal(0);

    chai.expect(calculateNumber('SUBTRACT', 0.5, 0)).to.equal(1);
    chai.expect(calculateNumber('SUBTRACT', 0, 0.5)).to.equal(-1);
    chai.expect(calculateNumber('SUBTRACT', 0.5, 0.5)).to.equal(0);

    chai.expect(calculateNumber('SUBTRACT', -0.5, 0)).to.equal(0);
    chai.expect(calculateNumber('SUBTRACT', 0, -0.5)).to.equal(0);
    chai.expect(calculateNumber('SUBTRACT', -0.5, -0.5)).to.equal(0);
  });
  it('divides rounded ``a`` by rounded ``b``, as ``Math.floor`` rounds', () => {
    chai.expect(calculateNumber('DIVIDE', 2, 2)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', 2, 1.5)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', 2, 1.25)).to.equal(2);
    chai.expect(calculateNumber('DIVIDE', 2, -1)).to.equal(-2);
    chai.expect(calculateNumber('DIVIDE', 2, -1.25)).to.equal(-2);
    chai.expect(calculateNumber('DIVIDE', 2, -1.5)).to.equal(-2);
    chai.expect(calculateNumber('DIVIDE', 2, -2)).to.equal(-1);

    chai.expect(calculateNumber('DIVIDE', 1.5, 2)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', 1.5, 1.5)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', 1.5, 1.25)).to.equal(2);
    chai.expect(calculateNumber('DIVIDE', 1.5, -1)).to.equal(-2);
    chai.expect(calculateNumber('DIVIDE', 1.5, -1.25)).to.equal(-2);
    chai.expect(calculateNumber('DIVIDE', 1.5, -1.5)).to.equal(-2);
    chai.expect(calculateNumber('DIVIDE', 1.5, -2)).to.equal(-1);

    chai.expect(calculateNumber('DIVIDE', 1.25, 2)).to.equal(0.5);
    chai.expect(calculateNumber('DIVIDE', 1.25, 1.5)).to.equal(0.5);
    chai.expect(calculateNumber('DIVIDE', 1.25, 1.25)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', 1.25, -1)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1.25, -1.25)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1.25, -1.5)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1.25, -2)).to.equal(-0.5);

    chai.expect(calculateNumber('DIVIDE', 1, 2)).to.equal(0.5);
    chai.expect(calculateNumber('DIVIDE', 1, 1.5)).to.equal(0.5);
    chai.expect(calculateNumber('DIVIDE', 1, 1.25)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', 1, -1)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1, -1.25)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1, -1.5)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1, -2)).to.equal(-0.5);

    chai.expect(calculateNumber('DIVIDE', -1, 2)).to.equal(-0.5);
    chai.expect(calculateNumber('DIVIDE', -1, 1.5)).to.equal(-0.5);
    chai.expect(calculateNumber('DIVIDE', -1, 1.25)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', -1, -1)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1, -1.25)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1, -1.5)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1, -2)).to.equal(0.5);

    chai.expect(calculateNumber('DIVIDE', -1.25, 2)).to.equal(-0.5);
    chai.expect(calculateNumber('DIVIDE', -1.25, 1.5)).to.equal(-0.5);
    chai.expect(calculateNumber('DIVIDE', -1.25, 1.25)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', -1.25, -1)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1.25, -1.25)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1.25, -1.5)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1.25, -2)).to.equal(0.5);

    chai.expect(calculateNumber('DIVIDE', -1.5, 2)).to.equal(-0.5);
    chai.expect(calculateNumber('DIVIDE', -1.5, 1.5)).to.equal(-0.5);
    chai.expect(calculateNumber('DIVIDE', -1.5, 1.25)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', -1.5, -1)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1.5, -1.25)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1.5, -1.5)).to.equal(1);
    chai.expect(calculateNumber('DIVIDE', -1.5, -2)).to.equal(0.5);

    chai.expect(calculateNumber('DIVIDE', -2, 2)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', -2, 1.5)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', -2, 1.25)).to.equal(-2);
    chai.expect(calculateNumber('DIVIDE', -2, -1)).to.equal(2);
    chai.expect(calculateNumber('DIVIDE', -2, -1.25)).to.equal(2);
    chai.expect(calculateNumber('DIVIDE', -2, -1.5)).to.equal(2);
    chai.expect(calculateNumber('DIVIDE', -2, -2)).to.equal(1);
  });
  it('Returns \'Error\' when rounded b is 0', () => {
    chai.expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', 0.25, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', 0, 0.25)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', 0.25, 0.25)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', 0.5, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', -0.25, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', -0.5, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', Infinity, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', -Infinity, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', NaN, 0)).to.equal('Error');
    chai.expect(calculateNumber('DIVIDE', -NaN, 0)).to.equal('Error');
  });
});
