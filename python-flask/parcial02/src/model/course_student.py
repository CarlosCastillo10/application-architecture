from src import db


class CourseStudent(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
