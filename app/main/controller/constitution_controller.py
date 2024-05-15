from flask_restx import Resource
from http import HTTPStatus
from app.main.service.search_service import SearchService
from flask import request
from app.main.controller.dto.constitution_dto import ConstitutionDto

api = ConstitutionDto.api
search_service = SearchService()


@api.route("/search")
class Constitution(Resource):
    @api.param("search_query")
    @api.param("page")
    @api.param("per_page")
    @api.param("section_name")
    @api.param("chapter_name")
    @api.param("section_number")
    @api.param("chapter_number")
    @api.param("article_number")
    @api.response(
        HTTPStatus.OK, description="Success", model=ConstitutionDto.search_response
    )
    def get(self):
        search_query = request.args.get("search_query", default="", type=str)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)
        section_name = request.args.get("section_name", default=None, type=str)
        chapter_name = request.args.get("chapter_name", default=None, type=str)
        section_number = request.args.get("section_number", default=None, type=int)
        chapter_number = request.args.get("chapter_number", default=None, type=int)
        article_number = request.args.get("article_number", default=None, type=int)
        return (
            search_service.constitution(
                search_query,
                page,
                per_page,
                section_name,
                chapter_name,
                section_number,
                chapter_number,
                article_number,
            ),
            HTTPStatus.OK,
        )
