from flask_restx import Resource
from http import HTTPStatus
from app.main.service.search_service import SearchService
from flask import request
from app.main.controller.dto.laws_dto import LawsDto

api = LawsDto.api
search_service = SearchService()


@api.route("/search")
class Laws(Resource):
    @api.param("search_query")
    @api.param("page")
    @api.param("per_page")
    @api.param("signature_start_date")
    @api.param("signature_end_date")
    @api.param("journal_start_date")
    @api.param("journal_end_date")
    @api.param("text_type")
    @api.param("text_number")
    @api.param("ministry")
    @api.param("field")
    @api.response(HTTPStatus.OK, description="Success", model=LawsDto.search_response)
    def get(self):
        search_query = request.args.get("search_query", default="", type=str)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)
        signature_start_date = request.args.get(
            "signature_start_date", default=None, type=str
        )
        signature_end_date = request.args.get(
            "signature_end_date", default=None, type=str
        )
        journal_start_date = request.args.get(
            "journal_start_date", default=None, type=str
        )
        journal_end_date = request.args.get("journal_end_date", default=None, type=str)
        text_type = request.args.get("text_type", default=None, type=str)
        text_number = request.args.get("text_number", default=None, type=str)
        ministry = request.args.get("ministry", default=None, type=str)
        field = request.args.get("field", default=None, type=str)
        return (
            search_service.laws(
                search_query,
                page,
                per_page,
                signature_start_date,
                signature_end_date,
                journal_start_date,
                journal_end_date,
                text_type,
                text_number,
                ministry,
                field,
            ),
            HTTPStatus.OK,
        )
