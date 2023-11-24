const assert = require('assert');
const calculateNumber = require('./0-calcul');

// (1.X) + (1.X)
assert.equal(calculateNumber(1, 1), 2);
assert.equal(calculateNumber(1.25, 1), 2);
assert.equal(calculateNumber(1, 1.25), 2);
assert.equal(calculateNumber(1.25, 1.25), 2);
assert.equal(calculateNumber(1.5, 1), 3);
assert.equal(calculateNumber(1, 1.5), 3);
assert.equal(calculateNumber(1.5, 1.5), 4);
// (-1.X) + (-1.X)
assert.equal(calculateNumber(-1, -1), -2);
assert.equal(calculateNumber(-1.25, -1), -2);
assert.equal(calculateNumber(-1, -1.25), -2);
assert.equal(calculateNumber(-1.25, -1.25), -2);
assert.equal(calculateNumber(-1.5, -1), -2);
assert.equal(calculateNumber(-1, -1.5), -2);
assert.equal(calculateNumber(-1.5, -1.5), -2);
// (2.X) + (2.X)
assert.equal(calculateNumber(2, 2), 4);
assert.equal(calculateNumber(2.25, 2), 4);
assert.equal(calculateNumber(2, 2.25), 4);
assert.equal(calculateNumber(2.25, 2.25), 4);
assert.equal(calculateNumber(2.5, 2), 5);
assert.equal(calculateNumber(2, 2.5), 5);
assert.equal(calculateNumber(2.5, 2.5), 6);
// (-2.X) + (-2.X)
assert.equal(calculateNumber(-2, -2), -4);
assert.equal(calculateNumber(-2.25, -2), -4);
assert.equal(calculateNumber(-2, -2.25), -4);
assert.equal(calculateNumber(-2.25, -2.25), -4);
assert.equal(calculateNumber(-2.5, -2), -4);
assert.equal(calculateNumber(-2, -2.5), -4);
assert.equal(calculateNumber(-2.5, -2.5), -4);
// Infinities
assert.equal(calculateNumber(Infinity, Infinity), Infinity);
assert.equal(calculateNumber(-Infinity, Infinity), NaN);
assert.equal(calculateNumber(Infinity, -Infinity), NaN);
assert.equal(calculateNumber(-Infinity, -Infinity), -Infinity);
// NaNs
assert.equal(calculateNumber(NaN, NaN), NaN);
assert.equal(calculateNumber(-NaN, NaN), NaN);
assert.equal(calculateNumber(NaN, -NaN), NaN);
assert.equal(calculateNumber(-NaN, -NaN), NaN);
// undefineds
assert.equal(calculateNumber(undefined, undefined), NaN);
assert.equal(calculateNumber(-undefined, undefined), NaN);
assert.equal(calculateNumber(undefined, -undefined), NaN);
assert.equal(calculateNumber(-undefined, -undefined), NaN);
