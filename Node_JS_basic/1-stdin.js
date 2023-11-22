process.on('exit', (code) => {
  console.log('This important software is now closing');
});

const readline = require('readline')
  .createInterface({
    input: process.stdin,
    output: process.stdout,
  });

readline.question(
  'Welcome to Holberton School, what is your name?',
  (name) => {
    console.log(`Your name is: ${name}`);
  },
);
