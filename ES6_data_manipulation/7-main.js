/* eslint-disable import/extensions */
import hasValuesFromArray from './7-has_array_values.js';

/*
true
false
false
true
true
true
false
false
*/
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [10]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1, 10]));
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), []));
console.log(hasValuesFromArray(new Set([]), []));
console.log(hasValuesFromArray(new Set(), []));
console.log(hasValuesFromArray(new Set([]), [1, 2, 3]));
console.log(hasValuesFromArray(new Set(), [1, 2, 3]));
