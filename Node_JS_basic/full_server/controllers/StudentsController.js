import readDatabase from '../utils.js';

const databaseFileName = process.argv[2];

export default class StudentsController {
	static async getAllStudents(request, response) {
		let studentsByMajor;
		try {
			studentsByMajor = await readDatabase(databaseFileName);
		} catch (error) {
			console.log(error);

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
		let studentsByMajor;
		try {
			studentsByMajor = await readDatabase(databaseFileName);
		} catch (error) {
			console.log(error);

			response.status(500);
			response.send('Cannot load the database');
			return;
		}

		const url_major = request.params.major;

		if (url_major === undefined) {
			response.status(500);
			response.send('Must input `major` URL parameter');
		} else if (url_major === 'CS' || url_major === 'SWE') {
			const studentsInMajorString = studentsByMajor[url_major].join(', ');
			response.send(`List: ${studentsInMajorString}`);
		} else {
			response.status(500);
			response.send('Major parameter must be CS or SWE');
		}
	}
};
