import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(request, response) {
    const databaseFileName = process.argv[2];

    let studentsByMajor;
    try {
      studentsByMajor = await readDatabase(databaseFileName);
    } catch (error) {
      // console.log(error);

      response.status(500);
      response.send('Cannot load the database');
      return;
    }

    let responseText = 'This is the list of our students';
    const majorsAlphabetized = Object.keys(studentsByMajor).sort();

    for (const major of majorsAlphabetized) {
      const studentsInMajor = studentsByMajor[major];

      responseText += `\nNumber of students in ${major}: ${studentsInMajor.length}. List: ${studentsInMajor.join(', ')}`;
    }

    response.send(responseText);
  }

  static async getAllStudentsByMajor(request, response) {
    const databaseFileName = process.argv[2];

    let studentsByMajor;
    try {
      studentsByMajor = await readDatabase(databaseFileName);
    } catch (error) {
      // console.log(error);

      response.status(500);
      response.send('Cannot load the database');
      return;
    }

    const urlMajor = request.params.major;

    if (urlMajor === undefined) {
      response.status(500);
      response.send('`major` URL param missing.');
    } else if (urlMajor === 'CS' || urlMajor === 'SWE') {
      const studentsInMajorString = studentsByMajor[urlMajor].join(', ');
      response.send(`List: ${studentsInMajorString}`);
    } else {
      response.status(500);
      response.send('Major parameter must be CS or SWE');
    }
  }
}
