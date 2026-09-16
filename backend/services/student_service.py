from models.student_model import Student
from repository.student_repository import StudentRepository


class StudentService:

    def __init__(self):
        self.repository = StudentRepository()

    def get_students(self, db):
        return self.repository.get_all(db)

    def get_student(self, db, student_id):
        return self.repository.get_by_id(db, student_id)

    def insert_student(self, db, request):

        student = Student(
            name=request.name,
            age=request.age,
            email=request.email,          # <-- Added
            department=request.department
        )

        return self.repository.insert(db, student)

    def update_student(self, db, student_id, request):

        student = self.repository.get_by_id(db, student_id)

        if student is None:
            return None

        student.name = request.name
        student.age = request.age
        student.email = request.email    # <-- Added
        student.department = request.department

        return self.repository.update(db, student)

    def delete_student(self, db, student_id):

        student = self.repository.get_by_id(db, student_id)

        if student is None:
            return False

        self.repository.delete(db, student)

        return True