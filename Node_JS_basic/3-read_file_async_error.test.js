const { expect } = require('chai');
const sinon = require('sinon');

const countStudents = require('./3-read_file_async.js');

describe('countStudents', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    consoleSpy.restore();
  });
  
  it('throws the correct error message', (done) => {
    countStudents('./blabl.csv')
      .catch((error) => {
        expect(error).to.equal(new Error('Error: Cannot load the database'));
      });
    expect(consoleSpy.calledWith('Number of students: 10')).to.not.be.true;
    expect(consoleSpy.calledWith('Number of students in CS: 6. List: Johenn, Arielle, Jonathen, Emmenuel, Guillaume, Katie')).to.not.be.true;
    expect(consoleSpy.calledWith('Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy')).to.not.be.true;

    done();
  });
});
