/* eslint-disable */
import guardrail from './9-try';
import divideFunction from './8-try';
/* eslint-enable */

test("guardrail catch errors", () => {
  expect(guardrail(() => divideFunction(10, 1))).toEqual([
    10,
    'Guardrail was processed',
  ]);

  expect(guardrail(() => divideFunction(10, 0))).toEqual([
    'Error: cannot divide by 0',
    'Guardrail was processed',
  ]);
});
