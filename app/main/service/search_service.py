from elasticsearch import Elasticsearch
from typing import Any, List


class SearchService:
    def __init__(self):
        self.es = Elasticsearch(
            "https://localhost:9200",
            basic_auth=("elastic", "gRakNDvDTcg+puCVov5W"),
            verify_certs=False,
        )

    def _format_search_res(self, search_res, page, per_page) -> dict:
        res: dict[str, Any] = {"data": []}
        for hit in search_res.body["hits"]["hits"]:
            item = hit["_source"]
            item["_id"] = hit["_id"]
            res["data"].append(item)

        res["results"] = len(res["data"])
        res["page"] = page
        res["total_results"] = search_res.body["hits"]["total"]["value"]
        res["has_more"] = (page * per_page) < res["total_results"]
        return res

    def supreme_court_decisions(
        self,
        search_query: str,
        page: int,
        per_page: int,
        start_date: str | None,
        end_date: str | None,
        search_field: str | None,
        subject: str | None,
        number: int | None,
    ):
        filters: List[dict[str, Any]] = []
        if start_date:
            filters.append({"range": {"date": {"gte": start_date}}})
        if end_date:
            filters.append({"range": {"date": {"lte": end_date}}})
        if subject:
            filters.append({"term": {"subject.keyword": {"value": subject}}})
        if number:
            filters.append({"term": {"number": {"value": number}}})

        if search_query == "":
            match_query: dict[str, Any] = {"match_all": {}}
        # search by specific field
        elif search_field:
            match_query = {"match": {search_field: search_query}}
        # multi field search
        else:
            match_query = {
                "multi_match": {
                    "query": search_query,
                    "fields": [
                        "subject",
                        "parties",
                        "keywords",
                        "reference",
                        "principle",
                        "ground_of_appeal",
                        "supreme_court_response",
                        "verdict",
                        "president",
                        "reporting_judge",
                    ],
                }
            }

        es_query = {
            "query": {
                "bool": {
                    "must": match_query,
                    "filter": filters,
                }
            },
            "from": (page - 1) * per_page,
            "size": per_page,
        }
        search_res = self.es.search(index="supreme-court", body=es_query)

        return self._format_search_res(search_res, page, per_page)
