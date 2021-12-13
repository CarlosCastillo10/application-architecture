from flask import request
from src.model.faculty import Faculty


class FacultyRepository:

    def get_departments_by_faculty(self, id):
        departments_db = Faculty.query.filter_by(id=id).first().departments
        departments = []

        for department in departments_db:
            department = department.serialize
            department['links'] = [
                self.add_link(
                    rel="self",
                    href="{}/department/{}".format(self.get_request_url(), department['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="degree",
                    href="{}/department/{}/degrees".format(self.get_request_url(), department['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="faculty",
                    href="{}/faculty/{}".format(self.get_request_url(), id),
                    action="GET"
                )
            ]
            departments.append(department)
        return departments

    def search_faculty_by_id(self, id):
        faculty_db = Faculty.query.filter_by(id=id).first()
        faculty = faculty_db.serialize
        faculty['links'] = [
            self.add_link(
                rel="department",
                href="{}/departments".format(request.url),
                action="GET"
            ),
            self.add_link(
                rel="root",
                href="{}/knowledge-area/{}/faculties".format(self.get_request_url(), faculty_db.knowledge_area_id),
                action="GET"
            )
        ]

        return faculty

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
