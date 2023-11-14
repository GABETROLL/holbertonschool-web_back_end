/* eslint-disable */
import handleResponseFromAPI from './2-then.js';
/* eslint-enable */

const promise = Promise.resolve();
const result = handleResponseFromAPI(promise);
console.log(result);
