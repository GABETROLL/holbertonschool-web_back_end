const calculateNumber = require('./1-calcul');
const assert = require('assert');

describe('calculateNumber', () => {
  it('sums rounded ``a`` and rounded ``b``, as ``Math.floor`` rounds', () => {
    assert.equal(calculateNumber('SUM', 0, 0), 0);

    assert.equal(calculateNumber('SUM', 0.25, 0), 0);
    assert.equal(calculateNumber('SUM', 0, 0.25), 0);
    assert.equal(calculateNumber('SUM', 0.25, 0.25), 0);

    assert.equal(calculateNumber('SUM', -0.25, 0), 0);
    assert.equal(calculateNumber('SUM', 0, -0.25), 0);
    assert.equal(calculateNumber('SUM', -0.25, -0.25), 0);

    assert.equal(calculateNumber('SUM', 0.5, 0), 1);
    assert.equal(calculateNumber('SUM', 0, 0.5), 1);
    assert.equal(calculateNumber('SUM', 0.5, 0.5), 2);
    
    assert.equal(calculateNumber('SUM', -0.5, 0), 0);
    assert.equal(calculateNumber('SUM', 0, -0.5), 0);
    assert.equal(calculateNumber('SUM', -0.5, -0.5), 0);
  });
  it('subtracts rounded ``b`` from rounded ``a``, as ``Math.floor`` rounds', () => {
    assert.equal(calculateNumber('SUBTRACT', 0, 0), 0);

    assert.equal(calculateNumber('SUBTRACT', 0.25, 0), 0);
    assert.equal(calculateNumber('SUBTRACT', 0, 0.25), 0);
    assert.equal(calculateNumber('SUBTRACT', 0.25, 0.25), 0);

    assert.equal(calculateNumber('SUBTRACT', -0.25, 0), 0);
    assert.equal(calculateNumber('SUBTRACT', 0, -0.25), 0);
    assert.equal(calculateNumber('SUBTRACT', -0.25, -0.25), 0);

    assert.equal(calculateNumber('SUBTRACT', 0.5, 0), 1);
    assert.equal(calculateNumber('SUBTRACT', 0, 0.5), -1);
    assert.equal(calculateNumber('SUBTRACT', 0.5, 0.5), 0);

    assert.equal(calculateNumber('SUBTRACT', -0.5, 0), 0);
    assert.equal(calculateNumber('SUBTRACT', 0, -0.5), 0);
    assert.equal(calculateNumber('SUBTRACT', -0.5, -0.5), 0);
  });
  it('divides rounded ``a`` by rounded ``b``, as ``Math.floor`` rounds', () => {
    assert.equal(calculateNumber('DIVIDE', 2, 2), 1);
    assert.equal(calculateNumber('DIVIDE', 2, 1.5), 1);
    assert.equal(calculateNumber('DIVIDE', 2, 1.25), 2);
    assert.equal(calculateNumber('DIVIDE', 2, -1), -2);
    assert.equal(calculateNumber('DIVIDE', 2, -1.25), -2);
    assert.equal(calculateNumber('DIVIDE', 2, -1.5), -2);
    assert.equal(calculateNumber('DIVIDE', 2, -2), -1);

    assert.equal(calculateNumber('DIVIDE', 1.5, 2), 1);
    assert.equal(calculateNumber('DIVIDE', 1.5, 1.5), 1);
    assert.equal(calculateNumber('DIVIDE', 1.5, 1.25), 2);
    assert.equal(calculateNumber('DIVIDE', 1.5, -1), -2);
    assert.equal(calculateNumber('DIVIDE', 1.5, -1.25), -2);
    assert.equal(calculateNumber('DIVIDE', 1.5, -1.5), -2);
    assert.equal(calculateNumber('DIVIDE', 1.5, -2), -1);

    assert.equal(calculateNumber('DIVIDE', 1.25, 2), 0.5);
    assert.equal(calculateNumber('DIVIDE', 1.25, 1.5), 0.5);
    assert.equal(calculateNumber('DIVIDE', 1.25, 1.25), 1);
    assert.equal(calculateNumber('DIVIDE', 1.25, -1), -1);
    assert.equal(calculateNumber('DIVIDE', 1.25, -1.25), -1);
    assert.equal(calculateNumber('DIVIDE', 1.25, -1.5), -1);
    assert.equal(calculateNumber('DIVIDE', 1.25, -2), -0.5);

    assert.equal(calculateNumber('DIVIDE', 1, 2), 0.5);
    assert.equal(calculateNumber('DIVIDE', 1, 1.5), 0.5);
    assert.equal(calculateNumber('DIVIDE', 1, 1.25), 1);
    assert.equal(calculateNumber('DIVIDE', 1, -1), -1);
    assert.equal(calculateNumber('DIVIDE', 1, -1.25), -1);
    assert.equal(calculateNumber('DIVIDE', 1, -1.5), -1);
    assert.equal(calculateNumber('DIVIDE', 1, -2), -0.5);

    assert.equal(calculateNumber('DIVIDE', -1, 2), -0.5);
    assert.equal(calculateNumber('DIVIDE', -1, 1.5), -0.5);
    assert.equal(calculateNumber('DIVIDE', -1, 1.25), -1);
    assert.equal(calculateNumber('DIVIDE', -1, -1), 1);
    assert.equal(calculateNumber('DIVIDE', -1, -1.25), 1);
    assert.equal(calculateNumber('DIVIDE', -1, -1.5), 1);
    assert.equal(calculateNumber('DIVIDE', -1, -2), 0.5);

    assert.equal(calculateNumber('DIVIDE', -1.25, 2), -0.5);
    assert.equal(calculateNumber('DIVIDE', -1.25, 1.5), -0.5);
    assert.equal(calculateNumber('DIVIDE', -1.25, 1.25), -1);
    assert.equal(calculateNumber('DIVIDE', -1.25, -1), 1);
    assert.equal(calculateNumber('DIVIDE', -1.25, -1.25), 1);
    assert.equal(calculateNumber('DIVIDE', -1.25, -1.5), 1);
    assert.equal(calculateNumber('DIVIDE', -1.25, -2), 0.5);

    assert.equal(calculateNumber('DIVIDE', -1.5, 2), -0.5);
    assert.equal(calculateNumber('DIVIDE', -1.5, 1.5), -0.5);
    assert.equal(calculateNumber('DIVIDE', -1.5, 1.25), -1);
    assert.equal(calculateNumber('DIVIDE', -1.5, -1), 1);
    assert.equal(calculateNumber('DIVIDE', -1.5, -1.25), 1);
    assert.equal(calculateNumber('DIVIDE', -1.5, -1.5), 1);
    assert.equal(calculateNumber('DIVIDE', -1.5, -2), 0.5);

    assert.equal(calculateNumber('DIVIDE', -2, 2), -1);
    assert.equal(calculateNumber('DIVIDE', -2, 1.5), -1);
    assert.equal(calculateNumber('DIVIDE', -2, 1.25), -2);
    assert.equal(calculateNumber('DIVIDE', -2, -1), 2);
    assert.equal(calculateNumber('DIVIDE', -2, -1.25), 2);
    assert.equal(calculateNumber('DIVIDE', -2, -1.5), 2);
    assert.equal(calculateNumber('DIVIDE', -2, -2), 1);
  });
  it('Returns \'Error\' when rounded b is 0', () => {
    assert.equal(calculateNumber('DIVIDE', 0, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', 0.25, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', 0, 0.25), 'Error');
    assert.equal(calculateNumber('DIVIDE', 0.25, 0.25), 'Error');
    assert.equal(calculateNumber('DIVIDE', 0.5, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -0.25, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -0.5, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', Infinity, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -Infinity, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', NaN, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -NaN, 0), 'Error');
  });
});
