export default function getResponseFromAPI() {
  function settlePromise(resolve, reject) { // eslint-disable-line no-unused-vars
    resolve('did nothing');
  }

  return new Promise(settlePromise);
}
