/*
Write and export a function named loadBalancer.
It should accept two arguments chinaDownload (Promise) and USDownload (Promise).

The function should return the value returned by the promise that resolved the first.

Prototype:

export default function loadBalancer(chinaDownload, USDownload) {

}
*/
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.any([chinaDownload, USDownload]);
}
