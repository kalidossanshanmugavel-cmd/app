from models.student_model import Student


class StudentRepository:

    def get_all(self, db):
        return db.query(Student).all()


    def get_by_id(self, db, student_id):

        return db.query(Student)\
                 .filter(Student.id == student_id)\
                 .first()


    def insert(self, db, student):

        db.add(student)

        db.commit()

        db.refresh(student)

        return student


    def update(self, db, student):

        db.commit()

        db.refresh(student)

        return student


    def delete(self, db, student):

        db.delete(student)

        db.commit()