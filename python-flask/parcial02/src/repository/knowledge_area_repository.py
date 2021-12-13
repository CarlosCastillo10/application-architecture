from flask import request
from src.model.knowledge_area import KnowledgeArea


class KnowledgeAreaRepository:

    def get_knowledge_areas(self):
        knowledge_areas_db = KnowledgeArea.query.all()
        knowledge_areas = []

        for knowledge_area in knowledge_areas_db:
            knowledge_area = knowledge_area.serialize
            knowledge_area['links'] = [
                self.add_link(
                    rel="self",
                    href="{}/knowledge-area/{}".format(self.get_request_url(), knowledge_area['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="faculty",
                    href="{}/knowledge-area/{}/faculties".format(self.get_request_url(), knowledge_area['id']),
                    action="GET"
                )
            ]
            knowledge_areas.append(knowledge_area)

        return knowledge_areas

    def get_faculties_by_knowledge_area(self, id):
        faculties_db = KnowledgeArea.query.filter_by(id=id).first().faculties
        faculties = []

        for faculty in faculties_db:
            faculty = faculty.serialize
            faculty['links'] = [
                self.add_link(
                    rel="self",
                    href="{}/faculty/{}".format(self.get_request_url(), faculty['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="department",
                    href="{}/faculty/{}/departments".format(self.get_request_url(), faculty['id']),
                    action="GET"
                ),
                self.add_link(
                    rel="root",
                    href="{}/knowledge-area/{}".format(self.get_request_url(), id),
                    action="GET"
                )
            ]
            faculties.append(faculty)
        return faculties

    def search_knowledge_area_by_id(self, id):
        knowledge_area = KnowledgeArea.query.filter_by(id=id).first().serialize
        knowledge_area['links'] = [
            self.add_link(
                rel="faculty",
                href="{}/faculties".format(request.url),
                action="GET"
            ),
            self.add_link(
                rel="root",
                href="{}/knowledge-areas".format(self.get_request_url()),
                action="GET"
            )
        ]

        return knowledge_area

    @staticmethod
    def add_link(rel, href, action):
        return {
            "rel": rel,
            "href": href,
            "action": action
        }

    @staticmethod
    def get_request_url():
        return '{}://{}'.format(request.scheme, request.environ['HTTP_HOST'])
