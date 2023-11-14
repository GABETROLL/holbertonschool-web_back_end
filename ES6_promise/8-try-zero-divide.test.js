/* eslint-disable */
import divideFunction from './8-try.js';
/* eslint-enable */

test('divideFunction throw an error', () => {
  expect(() => {
    divideFunction(10, 0);
  }).toThrowError('cannot divide by 0');
});
