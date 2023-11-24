const calculateNumber = require('./1-calcul');
const assert = require('assert');

describe('calculateNumber', () => {
  it('sums rounded ``a`` and rounded ``b``, as ``Math.floor`` rounds', () => {
    assert.equal(calculateNumber(0, 0, 'SUM'), 0);

    assert.equal(calculateNumber(0.25, 0, 'SUM'), 0);
    assert.equal(calculateNumber(0, 0.25, 'SUM'), 0);
    assert.equal(calculateNumber(0.25, 0.25, 'SUM'), 0);

    assert.equal(calculateNumber(-0.25, 0, 'SUM'), 0);
    assert.equal(calculateNumber(0, -0.25, 'SUM'), 0);
    assert.equal(calculateNumber(-0.25, -0.25, 'SUM'), 0);

    assert.equal(calculateNumber(0.5, 0, 'SUM'), 1);
    assert.equal(calculateNumber(0, 0.5, 'SUM'), 1);
    assert.equal(calculateNumber(0.5, 0.5, 'SUM'), 2);
    
    assert.equal(calculateNumber(-0.5, 0, 'SUM'), 0);
    assert.equal(calculateNumber(0, -0.5, 'SUM'), 0);
    assert.equal(calculateNumber(-0.5, -0.5, 'SUM'), 0);
  });
  it('subtracts rounded ``b`` from rounded ``a``, as ``Math.floor`` rounds', () => {
    assert.equal(calculateNumber(0, 0, 'SUBTRACT'), 0);

    assert.equal(calculateNumber(0.25, 0, 'SUBTRACT'), 0);
    assert.equal(calculateNumber(0, 0.25, 'SUBTRACT'), 0);
    assert.equal(calculateNumber(0.25, 0.25, 'SUBTRACT'), 0);

    assert.equal(calculateNumber(-0.25, 0, 'SUBTRACT'), 0);
    assert.equal(calculateNumber(0, -0.25, 'SUBTRACT'), 0);
    assert.equal(calculateNumber(-0.25, -0.25, 'SUBTRACT'), 0);

    assert.equal(calculateNumber(0.5, 0, 'SUBTRACT'), 1);
    assert.equal(calculateNumber(0, 0.5, 'SUBTRACT'), -1);
    assert.equal(calculateNumber(0.5, 0.5, 'SUBTRACT'), 0);

    assert.equal(calculateNumber(-0.5, 0, 'SUBTRACT'), 0);
    assert.equal(calculateNumber(0, -0.5, 'SUBTRACT'), 0);
    assert.equal(calculateNumber(-0.5, -0.5, 'SUBTRACT'), 0);
  });
  it('divides rounded ``a`` by rounded ``b``, as ``Math.floor`` rounds', () => {
    assert.equal(calculateNumber(2, 2, 'DIVIDE'), 1);
    assert.equal(calculateNumber(2, 1.5, 'DIVIDE'), 1);
    assert.equal(calculateNumber(2, 1.25, 'DIVIDE'), 2);
    assert.equal(calculateNumber(2, -1, 'DIVIDE'), -2);
    assert.equal(calculateNumber(2, -1.25, 'DIVIDE'), -2);
    assert.equal(calculateNumber(2, -1.5, 'DIVIDE'), -2);
    assert.equal(calculateNumber(2, -2, 'DIVIDE'), -1);

    assert.equal(calculateNumber(1.5, 2, 'DIVIDE'), 1);
    assert.equal(calculateNumber(1.5, 1.5, 'DIVIDE'), 1);
    assert.equal(calculateNumber(1.5, 1.25, 'DIVIDE'), 2);
    assert.equal(calculateNumber(1.5, -1, 'DIVIDE'), -2);
    assert.equal(calculateNumber(1.5, -1.25, 'DIVIDE'), -2);
    assert.equal(calculateNumber(1.5, -1.5, 'DIVIDE'), -2);
    assert.equal(calculateNumber(1.5, -2, 'DIVIDE'), -1);

    assert.equal(calculateNumber(1.25, 2, 'DIVIDE'), 0.5);
    assert.equal(calculateNumber(1.25, 1.5, 'DIVIDE'), 0.5);
    assert.equal(calculateNumber(1.25, 1.25, 'DIVIDE'), 1);
    assert.equal(calculateNumber(1.25, -1, 'DIVIDE'), -1);
    assert.equal(calculateNumber(1.25, -1.25, 'DIVIDE'), -1);
    assert.equal(calculateNumber(1.25, -1.5, 'DIVIDE'), -1);
    assert.equal(calculateNumber(1.25, -2, 'DIVIDE'), -0.5);

    assert.equal(calculateNumber(1, 2, 'DIVIDE'), 0.5);
    assert.equal(calculateNumber(1, 1.5, 'DIVIDE'), 0.5);
    assert.equal(calculateNumber(1, 1.25, 'DIVIDE'), 1);
    assert.equal(calculateNumber(1, -1, 'DIVIDE'), -1);
    assert.equal(calculateNumber(1, -1.25, 'DIVIDE'), -1);
    assert.equal(calculateNumber(1, -1.5, 'DIVIDE'), -1);
    assert.equal(calculateNumber(1, -2, 'DIVIDE'), -0.5);

    assert.equal(calculateNumber(-1, 2, 'DIVIDE'), -0.5);
    assert.equal(calculateNumber(-1, 1.5, 'DIVIDE'), -0.5);
    assert.equal(calculateNumber(-1, 1.25, 'DIVIDE'), -1);
    assert.equal(calculateNumber(-1, -1, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1, -1.25, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1, -1.5, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1, -2, 'DIVIDE'), 0.5);

    assert.equal(calculateNumber(-1.25, 2, 'DIVIDE'), -0.5);
    assert.equal(calculateNumber(-1.25, 1.5, 'DIVIDE'), -0.5);
    assert.equal(calculateNumber(-1.25, 1.25, 'DIVIDE'), -1);
    assert.equal(calculateNumber(-1.25, -1, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1.25, -1.25, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1.25, -1.5, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1.25, -2, 'DIVIDE'), 0.5);

    assert.equal(calculateNumber(-1.5, 2, 'DIVIDE'), -0.5);
    assert.equal(calculateNumber(-1.5, 1.5, 'DIVIDE'), -0.5);
    assert.equal(calculateNumber(-1.5, 1.25, 'DIVIDE'), -1);
    assert.equal(calculateNumber(-1.5, -1, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1.5, -1.25, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1.5, -1.5, 'DIVIDE'), 1);
    assert.equal(calculateNumber(-1.5, -2, 'DIVIDE'), 0.5);

    assert.equal(calculateNumber(-2, 2, 'DIVIDE'), -1);
    assert.equal(calculateNumber(-2, 1.5, 'DIVIDE'), -1);
    assert.equal(calculateNumber(-2, 1.25, 'DIVIDE'), -2);
    assert.equal(calculateNumber(-2, -1, 'DIVIDE'), 2);
    assert.equal(calculateNumber(-2, -1.25, 'DIVIDE'), 2);
    assert.equal(calculateNumber(-2, -1.5, 'DIVIDE'), 2);
    assert.equal(calculateNumber(-2, -2, 'DIVIDE'), 1);
  });
  it('Returns \'Error\' when rounded b is 0', () => {
    assert.equal(calculateNumber(0, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(0.25, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(0, 0.25, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(0.25, 0.25, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(0.5, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(-0.25, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(-0.5, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(Infinity, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(-Infinity, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(NaN, 0, 'DIVIDE'), 'Error');
    assert.equal(calculateNumber(-NaN, 0, 'DIVIDE'), 'Error');
  });
});
