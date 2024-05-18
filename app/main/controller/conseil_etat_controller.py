from flask_restx import Resource
from http import HTTPStatus
from app.main.service.search_service import SearchService
from flask import request
from app.main.controller.dto.conseil_dto import ConseilDto

api = ConseilDto.api
search_service = SearchService()


@api.route("/search")
class Conseil(Resource):
    @api.param("search_query")
    @api.param("page")
    @api.param("per_page")
    @api.param("chamber")
    @api.param("section")
    @api.param("procedure")
    @api.param("start_date")
    @api.param("end_date")
    @api.param("number")
    @api.response(
        HTTPStatus.OK, description="Success", model=ConseilDto.search_response
    )
    def get(self):
        search_query = request.args.get("search_query", default="", type=str)
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)
        number = request.args.get("number", default=None, type=int)
        chamber = request.args.get("chamber", default=None, type=str)
        section = request.args.get("section", default=None, type=str)
        procedure = request.args.get("procedure", default=None, type=str)
        start_date = request.args.get("start_date", default=None, type=str)
        end_date = request.args.get("end_date", default=None, type=str)
        return (
            search_service.conseil(
                search_query,
                page,
                per_page,
                number,
                chamber,
                section,
                procedure,
                start_date,
                end_date,
            ),
            HTTPStatus.OK,
        )
