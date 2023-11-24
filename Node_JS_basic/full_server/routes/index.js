/* eslint-disable import/extensions */
import AppController from '../controllers/AppController.js';
import StudentsController from '../controllers/StudentsController.js';

const routes = {
  '/': AppController.getHomepage,
  '/students': StudentsController.getAllStudents,
  '/students/:major': StudentsController.getAllStudentsByMajor,
};
export default routes;
