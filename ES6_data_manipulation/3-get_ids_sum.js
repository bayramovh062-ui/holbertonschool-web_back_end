export default function getStudentIdsSum(students) {
    return students.reduce((sumOfId, student) => sumOfId += student.id, 0)
} 