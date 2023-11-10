/*
Notice how the keys and the variable names are the same?
Modify the following function’s budget object
to simply use the keyname instead.

export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income: income,
    gdp: gdp,
    capita: capita,
  };

  return budget;
}
*/

export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income,
    gdp,
    capita,
  };

  return budget;
}
