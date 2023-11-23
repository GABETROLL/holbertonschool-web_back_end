const obj = {
  x: 42,
  something: () => {
    return this.x;
  },
};

class SomethingObj {
  something = () => {
    console.log(this);
  };
}
const sobj = new SomethingObj();

console.log(typeof obj.something);
console.log(typeof sobj.something);

console.log(obj.something);
obj.something = obj.something.bind(obj);
console.log(obj.something);

console.log(sobj.something);
sobj.something = sobj.something.bind(sobj);
console.log(sobj.something);

console.log(obj.something());
