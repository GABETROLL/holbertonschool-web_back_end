/*
Simple promise

Using the following prototype:
function signUpUser(firstName, lastName) {
}

That returns a resolved promise with this object:
{
  firstName: value,
  lastName: value,
}

Expected output:
Promise { { firstName: 'Bob', lastName: 'Dylan' } }
*/
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
