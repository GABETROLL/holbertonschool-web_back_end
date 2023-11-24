module.exports = function calculateNumber(a, b, type) {
  a = Math.round(a);
  b = Math.round(b);

  if (type === 'SUM') {
    return a + b;
  } else if (type === 'SUBTRACT') {
    return a - b;
  } else if (type === 'DIVIDE') {
    return b === 0 ? 'Error' : a / b;
  } else {
    return 'Error';
  }
}
