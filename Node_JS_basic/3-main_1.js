const countStudents = require('./3-read_file_async');

const result = countStudents('databasdasdase.csv');

throw new Error('test');

console.log(result);

result
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log('CAUGHT ERROR!');
    console.log(error);
  });

console.log('After!');
