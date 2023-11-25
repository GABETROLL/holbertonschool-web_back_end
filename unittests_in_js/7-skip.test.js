/*
When you have a long list of tests,
and you can’t figure out why a test is breaking,
avoid commenting out a test, or removing it.
Skip it instead, and file a ticket to come back to it
as soon as possible.
  - Make the test suite pass without fixing or removing the failing test
  - it description must stay the same
*/
const { expect } = require('chai');

describe('Testing numbers', () => {
  it('1 is equal to 1', () => {
    expect(1 === 1).to.be.true;
  });

  it('2 is equal to 2', () => {
    expect(2 === 2).to.be.true;
  });

  it('1 is equal to 3', function () {
    this.skip();
    expect(1 === 3).to.be.true;
  });

  it('3 is equal to 3', () => {
    expect(3 === 3).to.be.true;
  });

  it('4 is equal to 4', () => {
    expect(4 === 4).to.be.true;
  });

  it('5 is equal to 5', () => {
    expect(5 === 5).to.be.true;
  });

  it('6 is equal to 6', () => {
    expect(6 === 6).to.be.true;
  });

  it('7 is equal to 7', () => {
    expect(7 === 7).to.be.true;
  });
});
