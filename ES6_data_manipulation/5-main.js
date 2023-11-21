/* eslint-disable import/extensions */
import createInt8TypedArray from './5-typed_arrays.js';

// console.log(createInt8TypedArray(10, 2, 89));
// console.log(createInt8TypedArray(10, 2, 1000000));
// console.log(createInt8TypedArray(10, 11, 89));

const i = new Int8Array(10);
const b = new ArrayBuffer(10);
const v = new DataView(b);

console.log(i);
console.log(b);
console.log(v);

i[0] = 1;
i[1] = 2;
i[0.01] = 3;
i[3] = 1;
i[-10000] = NaN;
i[0] = NaN; // resets it to 0

console.log(i);

b[0] = 1;
b[1] = 2;
b[0.01] = 3;
b[3] = 1;
b[-10000] = NaN;
b[0] = NaN;

console.log(b);

v[69] = 69;

console.log(v);

v.setInt8(0, 1);
v.setInt8(1, 2);
// v.setInt8(-1, -1);
v.setInt8(3, -128);
// v.setInt8(30000, 11);
v.setInt8(9, 2222222222222);

console.log(v);

console.log(createInt8TypedArray(10, 2, 89));
console.log(createInt8TypedArray(10, 2, -10000));
console.log(createInt8TypedArray(10, 100000, 1));
