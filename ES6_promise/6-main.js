/* eslint-disable */
import handleProfileSignup from './6-final-user.js';
/* eslint-enable */

const promise = handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg')
  .then((result) => { console.log(result); });
console.log(promise);
