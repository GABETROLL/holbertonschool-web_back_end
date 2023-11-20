export default function getListStudentIds(students) {
  if (!(students instanceof Array)) {
    return [];
  }
  return students.map((student) => student.id);
}
