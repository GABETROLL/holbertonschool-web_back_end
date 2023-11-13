/* eslint-disable */
import getResponseFromAPI from "./0-promise.js";
/* eslint-enable */

const response = getResponseFromAPI();
console.log(response instanceof Promise);
