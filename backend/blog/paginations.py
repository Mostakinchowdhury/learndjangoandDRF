from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.response import Response

class mypagi(PageNumberPagination):
  page_size=2
  max_page_size=3
  page_query_param="p"
  page_size_query_param="ps"
  last_page_strings=["finish",]

  def get_paginated_response(self, data):
        return Response({
            "total_page":self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            "x-author":"Mostakin chowdhury",
            'previous': self.get_previous_link(),
            'results': data,})

class myoffpagi(LimitOffsetPagination):
  default_limit=2
  limit_query_param="l"
  max_limit=4
  offset_query_param="of"
  def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            "wife":"monira",
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

