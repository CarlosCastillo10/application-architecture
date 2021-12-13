from flask import request
from src.model.course import Course
from src.model.student import Student
from src.model.course_student import CourseStudent


class CourseStudentRepository:
    course_id = None

    def get_students_by_course(self, id):
        self.course_id = id
        students_db = Course.query.filter_by(id=id).first().students.all()
        students = []

        for student in students_db:
            student = student.serialize
            student['links'] = [
                self.add_link(
                    rel="self",
                    href="{}/student/{}".format(self.get_request_url(), student['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="course",
                    href="{}/course/{}".format(self.get_request_url(), id),
                    action="GET"
                )
            ]
            students.append(student)

        return students

    def search_course_by_id(self, id):
        self.course_id = id
        course_db = Course.query.filter_by(id=self.course_id).first()
        course = course_db.serialize
        course['links'] = [
            self.add_link(
                rel="student",
                href="{}/students".format(request.url),
                action="GET"
            ),
            self.add_link(
                rel="root",
                href="{}/degree/{}/courses".format(self.get_request_url(), course_db.degree_id),
                action="GET"
            )
        ]

        return course

    def search_student_by_id(self, id):
        student_db = Student.query.filter_by(id=id).first()
        student = student_db.serialize
        if self.course_id is None:
            student['links'] = [
                self.add_link(
                    rel="root", href="{}/course/{}/students".format(self.get_request_url(), course.id), action="GET"
                ) for course in student_db.courses.all()
            ]
        else:
            student['links'] = [
                self.add_link(
                    rel="root", href="{}/course/{}/students".format(self.get_request_url(), self.course_id),
                    action="GET"
                )
            ]
        return student

    @staticmethod
    def add_link(rel, href, action):
        return {
            "rel": rel,
            "href": href,
            "action": action
        }

    @staticmethod
    def get_request_url():
        return '{}://{}:{}'.format(request.scheme, request.server[0], request.server[-1])
