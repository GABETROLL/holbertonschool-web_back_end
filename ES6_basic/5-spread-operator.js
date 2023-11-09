/*
Using spread syntax,
concatenate 2 arrays and each character of a string
by modifying the function below.
Your function body should be one line long.
*/
export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}
