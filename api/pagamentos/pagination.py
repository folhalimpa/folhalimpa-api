from collections import OrderedDict
from rest_framework.response import Response
from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 635
