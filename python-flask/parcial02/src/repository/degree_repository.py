from flask import request
from src.model.degree import Degree


class DegreeRepository:

    def get_courses_by_degree(self, id):
        courses_db = Degree.query.filter_by(id=id).first().courses
        courses = []

        for course in courses_db:
            course = course.serialize
            course['links'] = [
                self.add_link(
                    rel="self",
                    href="{}/course/{}".format(self.get_request_url(), course['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="student",
                    href="{}/course/{}/students".format(self.get_request_url(), course['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="degree",
                    href="{}/degree/{}".format(self.get_request_url(), id),
                    action="GET"
                )
            ]
            courses.append(course)
        return courses

    def search_degree_by_id(self, id):
        degree_db = Degree.query.filter_by(id=id).first()
        degree = degree_db.serialize
        degree['links'] = [
            self.add_link(
                rel="course",
                href="{}/courses".format(request.url),
                action="GET"
            ),
            self.add_link(
                rel="root",
                href="{}/department/{}/degrees".format(self.get_request_url(), degree_db.department_id),
                action="GET"
            )
        ]

        return degree

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
