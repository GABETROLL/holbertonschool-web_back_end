/* eslint-disable import/extensions */
import hasValuesFromArray from "./7-has_array_values.js";

console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1]));     // true
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [10]));    // false
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), [1, 10])); // false
console.log(hasValuesFromArray(new Set([1, 2, 3, 4, 5]), []));      // true
console.log(hasValuesFromArray(new Set([]), []));                   // true
console.log(hasValuesFromArray(new Set(), []));                     // true
console.log(hasValuesFromArray(new Set([]), [1, 2, 3]));            // false
console.log(hasValuesFromArray(new Set(), [1, 2, 3]));              // false
