/*
Create a function, named ``getStudentIdsSum``,
  that returns the sum of all the student ids.
It should accept
  a list of students (from ``getListStudents``) as a parameter.

You must use the ``reduce`` function on the array.
*/
export default function getStudentIdsSum(students) {
  if (!(students instanceof Array)) {
    return [];
  }
  return students.reduce(
    ((result, student) => result + student.id),
    0,
  );
}
