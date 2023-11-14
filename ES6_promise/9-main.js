/* eslint-disable */
import guardrail from './9-try.js';
import divideFunction from './8-try.js';
/* eslint-enable */

/*
Expected output:

[ 5, 'Guardrail was processed' ]
[ 'Error: cannot divide by 0', 'Guardrail was processed' ]
*/
console.log(guardrail(() => divideFunction(10, 2)));
console.log(guardrail(() => divideFunction(10, 0)));
