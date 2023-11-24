import { readDatabase } from '../utils.js';

const databaseFileName = process.argv[2];

export default class StudentsController {
	static async getAllStudents(request, response) {
		let studentsByMajor;
		try {
			studentsByMajor = await readDatabase(databaseFileName);
		} catch (error) {
			response.status(500);
			response.send('Cannot load the database');
		}

		console.log(studentsByMajor);

		let responseText = 'This is the list of our students\n';
		const majorsAlphabetized = Object.keys(studentsByMajor).sort();

		for (const major of majorsAlphabetized) {
			const studentsInMajor = studentsByMajor[major];

			responseText += `Number of students in ${major}: ${studentsInMajor.length}. List: ${studentsInMajor}`;
		}

		response.send(responseText);
	}

	static async getAllStudentsByMajor(request, response) {
		let studentsByMajor;
		try {
			studentsByMajor = await readDatabase(databaseFileName);
		} catch (error) {
			response.status(500);
			response.send('Cannot load the database');
		}

		if (request.query.major === undefined) {
			response.status(500);
			response.send('Must input `major` URL parameter');
		} else if (request.query.major === 'CS' || request.query.major === 'SWE') {
			response.send(`List: ${studentsByMajor[request.query.major]}`);
		} else {
			response.status(500);
			response.send('Major parameter must be CS or SWE');
		}
	}
};
