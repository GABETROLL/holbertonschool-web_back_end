/*
Expected output:
{
  allEmployees: { engineering: [ 'Bob', 'Jane' ], marketing: [ 'Sylvie' ] },
  getNumberOfDepartments: [Function: getNumberOfDepartments]
}
{ engineering: [ 'Bob', 'Jane' ], marketing: [ 'Sylvie' ] }
2
*/
/* eslint-disable */
import createEmployeesObject from './11-createEmployeesObject.js';
import createReportObject from './12-createReportObject.js';
/* eslint-enable */

const employees = {
  ...createEmployeesObject('engineering', ['Bob', 'Jane']),
  ...createEmployeesObject('marketing', ['Sylvie']),
};

const report = createReportObject(employees);
console.log(report);
console.log(report.allEmployees);
console.log(report.getNumberOfDepartments(report.allEmployees));
