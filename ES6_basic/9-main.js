/* eslint-disable */
import getFullBudgetObject from './9-getFullBudget.js';
/* eslint-enable */

const fullBudget = getFullBudgetObject(20, 50, 10);

console.log(fullBudget);

console.log(fullBudget.getIncomeInDollars(fullBudget.income));
console.log(fullBudget.getIncomeInEuros(fullBudget.income));
