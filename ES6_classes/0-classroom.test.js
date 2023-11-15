/* eslint-disable */
import ClassRoom from './0-classroom.js';
/* eslint-enable */

test('Initialize an instance of ClassRoom set to 100', () => {
  const room = new ClassRoom(100);
  expect(room._maxStudentsSize).toBe(100);
});
