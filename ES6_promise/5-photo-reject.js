/*
Write and export a function named ``uploadPhoto``.
It should accept one argument named ``fileName`` (string).

The function should return a ``Promise`` rejecting with an ``Error``
  and the string `$fileName cannot be processed`.

export default function uploadPhoto(filename) {

}

Expected output:

Promise {
  <rejected> Error: guillaume.jpg cannot be processed
  ..
    ..
*/
export default function uploadPhoto(filename) {
  /*
  Same as:

  return new Promise(
    (resolve, reject) => {
      // mocking uploading photo here
      reject(
        new Error(`${filename} cannot be processed`)
      );
    }
  )
  */
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
