from math import ceil
from urllib.parse import urlencode
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class AppPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"
    page_size_query_param = "per_page"
    max_page_size = 100

    def _make_url(self, base_url, page_number):
        # recria os params a cada chamada para não vazar mutações
        qp = self.request.query_params.copy()
        qp[self.page_query_param] = page_number
        # garante que o per_page atual é preservado
        per_page = self.get_page_size(self.request)
        if per_page:
            qp[self.page_size_query_param] = per_page
        query_string = urlencode(qp, doseq=True)
        return f"{base_url}?{query_string}"

    def get_paginated_response(self, data):
        total = self.page.paginator.count
        per_page = self.get_page_size(self.request) or self.page.paginator.per_page                    
        current_page = self.page.number
        last_page = ceil(total / per_page) if per_page else 1

        base_url = self.request.build_absolute_uri(self.request.path)

        first_page_url = self._make_url(base_url, 1)
        last_page_url  = self._make_url(base_url, last_page)

        # next/prev do DRF já funcionam; apenas garantimos que preservam per_page
        next_page_url = self.get_next_link()
        prev_page_url = self.get_previous_link()

        return Response({
            "meta": {
                "total": total,
                "per_page": per_page,
                "current_page": current_page,
                "last_page": last_page,
                "first_page": 1,
                "first_page_url": first_page_url,
                "last_page_url": last_page_url,
                "next_page_url": next_page_url,
                "previous_page_url": prev_page_url,
            },
            "data": data,
        }) 