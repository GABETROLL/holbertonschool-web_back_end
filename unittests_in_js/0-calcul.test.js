const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('returns ``a + b`` when both ``a`` and ``b`` are whole numbers', () => {
    assert.equal(calculateNumber(1, 1), 2);
    assert.equal(calculateNumber(-1, -1), -2);
    assert.equal(calculateNumber(2, 2), 4);
    assert.equal(calculateNumber(-2, -2), -4);
  });
  it('rounds ``a``, like ``Math.round``, before adding it', () => {
    assert.equal(calculateNumber(1.25, 1), 2);
    assert.equal(calculateNumber(1.5, 1), 3);

    assert.equal(calculateNumber(-1.25, -1), -2);
    assert.equal(calculateNumber(-1.5, -1), -2);
  
    assert.equal(calculateNumber(2.25, 2), 4);
    assert.equal(calculateNumber(2.5, 2), 5);

    assert.equal(calculateNumber(-2.25, -2), -4);
    assert.equal(calculateNumber(-2.5, -2), -4);
  });
  it('rounds ``b``, like ``Math.round``, before adding it', () => {
    assert.equal(calculateNumber(1, 1.25), 2);
    assert.equal(calculateNumber(1, 1.5), 3);
    assert.equal(calculateNumber(-1, -1.25), -2);
    assert.equal(calculateNumber(-1, -1.5), -2);

    assert.equal(calculateNumber(2, 2.25), 4);
    assert.equal(calculateNumber(2, 2.5), 5);
    assert.equal(calculateNumber(-2, -2.25), -4);
    assert.equal(calculateNumber(-2, -2.5), -4);
  });
  it('rounds ``a`` and ``b``, like ``Math.round``, before adding them to eachother', () => {
    assert.equal(calculateNumber(1.25, 1.25), 2);
    assert.equal(calculateNumber(1.5, 1.5), 4);
    assert.equal(calculateNumber(-1.25, -1.25), -2);
    assert.equal(calculateNumber(-1.5, -1.5), -2);

    assert.equal(calculateNumber(2.25, 2.25), 4);
    assert.equal(calculateNumber(2.5, 2.5), 6);
    assert.equal(calculateNumber(-2.25, -2.25), -4);
    assert.equal(calculateNumber(-2.5, -2.5), -4);
  });
});
