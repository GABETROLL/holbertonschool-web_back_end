export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }
  set name(newName) {
    if (typeof newName !== 'string') {
      throw TypeError('`name` must be a string.');
    } this._name = newName;
  }

  get length() {
    return this._length;
  }
  set length(newLength) {
    if (typeof newLength !== 'number') {
      throw TypeError('`length` must be a number.');
    } this._length = newLength;
  }

  get students() {
    return this.students;
  }
  set students(newStudents) {
    if (typeof newStudents !== 'object') {
      throw TypeError('`students` must be an array of strings.');
    } this._students = newStudents;
  }
}
