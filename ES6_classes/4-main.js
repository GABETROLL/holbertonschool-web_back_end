/* eslint-enable */
import Pricing from './4-pricing.js';
import Currency from './3-currency.js';
/* eslint-disable */

const p = new Pricing(100, new Currency("EUR", "Euro"));
console.log(p);
console.log(p.displayFullPrice());
