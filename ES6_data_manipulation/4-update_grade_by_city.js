export default function updateStudentGradeByCity(students, city, newGrades) {
  const filteredStudents = students.filter((student) => student.location === city);
  
  return filteredStudents.map((student) => {
    let flag = false;
    for (const grade of newGrades) {
      if (grade.studentId === student.id) {
        student.grade = grade.grade;
        flag = true;
      }
    }
    if (!flag) {
      student.grade = 'N/A';
    }
    return student;
  });
}