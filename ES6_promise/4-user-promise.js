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

bob@dylan:~$ cat 4-main.js
import signUpUser from "./4-user-promise";

console.log(signUpUser("Bob", "Dylan"));

bob@dylan:~$ 
bob@dylan:~$ npm run dev 4-main.js 
Promise { { firstName: 'Bob', lastName: 'Dylan' } }
bob@dylan:~$ 
*/
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
