/*
expected output in stdout:
10
*/
/* eslint-disable */
import ClassRoom from './0-classroom.js';
/* eslint-enable */

const room = new ClassRoom(10);
console.log(room._maxStudentsSize);
