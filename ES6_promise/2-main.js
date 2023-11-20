/* eslint-disable */
import handleResponseFromAPI from './2-then.js';
/* eslint-enable */

const promise = Promise.reject();
handleResponseFromAPI(promise);
