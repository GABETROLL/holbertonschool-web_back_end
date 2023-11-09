/*
Rewrite the `getBudgetForCurrentYear` function
to use ES6 computed property names on the budget object.

function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {};

  budget[`income-${getCurrentYear()}`] = income;
  budget[`gdp-${getCurrentYear()}`] = gdp;
  budget[`capita-${getCurrentYear()}`] = capita;

  return budget;
}
*/

function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const incomeName = `income-${getCurrentYear()}`;
  const gdpName = `gdp-${getCurrentYear()}`;
  const capitaName = `capita-${getCurrentYear()}`;

  const budget = {
    [incomeName]: income,
    [gdpName]: gdp,
    [capitaName]: capita,
  };

  return budget;
}
