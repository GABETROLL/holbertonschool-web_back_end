/* eslint-disable import/extensions */
import setFromArray from './6-set.js';

const result = setFromArray([
  12, 0.2, -3, -3.14, NaN, -NaN, Infinity, -Infinity,
  'hi', '',
  true, false, null, undefined, -null, -undefined, -false, -true,
  [], [-1], [undefined],
  { }, { hi: 'hello', method() { return NaN; } },
  Symbol(''), Symbol(''),
  new Int8Array(10), new ArrayBuffer(10), new DataView(new ArrayBuffer(1)),
]);

console.log(result);
