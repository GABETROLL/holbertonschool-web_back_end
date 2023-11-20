/* eslint-disable */
import handleProfileSignup from './6-final-user.js';
/* eslint-enable */

const p = handleProfileSignup('Bob', 'Dylan', 'bob_dylan.jpg');
console.log(p);

(async () => console.log(await p))();
