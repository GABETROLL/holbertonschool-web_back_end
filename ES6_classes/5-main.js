/* eslint-disable */
import Building from './5-building.js';
/* eslint-enable */
let building = new Building(100);
console.log(building);

class TestBuilding extends Building {}

try {
  building = new TestBuilding(200);
} catch (error) {
  console.log(error.toString());
}

class OtherBuilding extends Building {
  /* eslint-disable class-methods-use-this */
  evacuationWarningMessage() {
    return 'Evacuate.';
  }
  /* eslint-enable class-methods-use-this */
}

building = new OtherBuilding(300);
console.log(building.evacuationWarningMessage());
