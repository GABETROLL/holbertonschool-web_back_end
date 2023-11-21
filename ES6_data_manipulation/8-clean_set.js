/*
Create a function, named ``cleanSet``,
  that returns a string of all the set values
  that start with a specific string (``startString``).

It accepts two arguments:
  a ``set`` (Set)
  and a ``startString`` (String).

When a value starts with ``startString``,
  you only append the rest of the string.
  The string contains all the values of the set,
  separated by '-'.

(IF AN ITEM ISN'T A STRING, IT'S IGNORED)
(IF ``startString`` ISN'T A STRING OR IS AN EMPTY STRING,
THIS FUNCTION RETURNS '')
*/
export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  // turning the set into an array of all of the items
  // that are strings and that start with ``startString``,
  // without the ``startString`` as their start,
  // THEN returning ``resultArray.join('-')``.
  const resultArray = [];

  set.forEach((item) => {
    // ignoring the item,
    // by not appending it to the items array.
    if (typeof item === 'string' && item.startsWith(startString)) {
      resultArray.push(
        item.substring(
          startString.length, item.length,
        ),
      );
    }
  });

  return resultArray.join('-');
}
