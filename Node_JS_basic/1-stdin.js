function end() {
  process.stdout.write('This important software is now closing\r');
}
process.on('exit', end);
process.on('SIGINT', end);

const readline = require('readline')
  .createInterface({
    input: process.stdin,
    output: process.stdout,
  });

readline.question(
  'Welcome to Holberton School, what is your name?\n',
  (name) => {
    process.stdout.write(`Your name is: ${name}\r`);
  },
);
