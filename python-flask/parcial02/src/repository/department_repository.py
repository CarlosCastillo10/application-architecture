from flask import request
from src.model.department import Department


class DepartmentRepository:

    def get_degrees_by_department(self, id):
        degrees_db = Department.query.filter_by(id=id).first().degrees
        degrees = []

        for degree in degrees_db:
            degree = degree.serialize
            degree['links'] = [
                self.add_link(
                    rel="self",
                    href="{}/degree/{}".format(self.get_request_url(), degree['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="course",
                    href="{}/degree/{}/courses".format(self.get_request_url(), degree['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="department",
                    href="{}/department/{}".format(self.get_request_url(), id),
                    action="GET"
                )
            ]
            degrees.append(degree)
        return degrees

    def search_department_by_id(self, id):
        department_db = Department.query.filter_by(id=id).first()
        department = department_db.serialize
        department['links'] = [
            self.add_link(
                rel="degree",
                href="{}/degrees".format(request.url),
                action="GET"
            ),
            self.add_link(
                rel="root",
                href="{}/faculty/{}/departments".format(self.get_request_url(), department_db.faculty_id),
                action="GET"
            )
        ]

        return department

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
