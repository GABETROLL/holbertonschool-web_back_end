import { uploadPhoto, createUser } from "./utils.js";

export default function handleProfileSignup() {
  function handleResolve (result) {
    console.log(result[0].body, result[1].firstName, result[1].lastName);
  }
  function handleError (error) {
    console.log('Signup system offline');
  }

  return Promise.all([uploadPhoto(), createUser()])
    .then(handleResolve, handleError);
}
