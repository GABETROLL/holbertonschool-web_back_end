/* eslint-disable import/extensions */
import cleanSet from './8-clean_set.js';

console.log((new Set([0, 1, 2])).entries());
// (new Set(...)).entries() doesn't return an array...
// And Array(new Set(...)) doesn't give you an array of
//  all of the set's items...
// Neither does Array((new Set(...)).entries()) .

console.log('string'.startsWith(''));
// true. But we want ``cleanSet`` to not count '' as a valid
// startString to any of the set's strings.

console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), 'bon'));
// should be 'jovi-aparte-appetit'.
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), ''));
// should be ''.
console.log(cleanSet(new Set(['id-test', 'id-chicken', 'id-user', , 'id-id-']), 'id-'));
// should be 'test-chicken-user-id-'.                        NaN ^
// If an item in the set isn't a string, it's IGNORED.
console.log(cleanSet(new Set(['bonjovi', 'bonaparte', 'bonappetit', 'banana']), []));
// should also be '', since a ``startString`` argument
// that isn't a string should automatically make ``cleanSet``
// return ''.
