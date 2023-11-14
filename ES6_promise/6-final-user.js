/*
Import ``signUpUser`` from ``4-user-promise.js``
  and ``uploadPhoto`` from ``5-photo-reject.js``.

Write and export a function named ``handleProfileSignup``.
It should accept three arguments:
 - ``firstName`` (string)
 - ``lastName`` (string)
 - ``fileName`` (string).
The function should call the two other functions.
When the promises are all settled,
it should return an array with the following structure:
[
    {
      status: status_of_the_promise,
      value: value or error returned by the Promise
    },
    ...
  ]

Expected output:

Promise { <pending> }
*/
/* eslint-disable */
import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';
/* eslint-enable */

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]);
}
