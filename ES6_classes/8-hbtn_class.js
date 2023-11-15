/*
Implement a class named HolbertonClass:
  - Constructor attributes:
    - size (Number)
    - location (String)
  - Each attribute must be stored in an “underscore” attribute version (ex: name is stored in _name)
  - When the class is cast into a Number, it should return the size.
  - When the class is cast into a String, it should return the location.
*/

export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() { // to cast this to int: ``this._size``
    return this._size;
  }

  toString() { // to cast this to string: ``this._location``
    return this._location;
  }
}
