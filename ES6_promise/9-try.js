/*
Write a function named guardrail
that will accept one argument named ``mathFunction`` (Function).

This function should create and return an array named queue.

When the mathFunction function is executed,
the value returned by the function should be appended to the queue.
If this function throws an error,
the error message should be appended to the queue.
In every case, the message 'Guardrail was processed'
should be added to the queue.

Examples: (``divideFunction`` is from the previous exercise)

guardrail(() => { return divideFunction(10, 2)})
outputs:
[ 1000, 'Guardrail was processed' ]

guardrail(() => { return divideFunction(10, 0)})
outputs:
[ 'Error: cannot divide by 0', 'Guardrail was processed' ]
*/
export default function guardrail(mathFunction) {
  const queue = [];

  try {
    queue.push(mathFunction());
  } catch (error) {
    queue.push(error.toString());
  }

  queue.push('Guardrail was processed');

  return queue;
}
