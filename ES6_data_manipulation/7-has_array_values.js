/*
Create a function, named ``hasValuesFromArray``,
  that returns a boolean if all the elements in the array 
  exist within the set.

It accepts two arguments:
  a set (Set)
  and an array (Array). 
*/
export default function hasValuesFromArray(set, array) {
  // for every item in ``array``: check that it's present in ``set``.
  // If even one item in ``array`` isn't present in set, return false.
  return array.every((item) => set.has(item));
}
