from rest_framework.pagination import CursorPagination


class MyCustomCursorPagination(CursorPagination):
    ordering = '-id'
    page_size = 10

class CreatedAtCursorPagination(CursorPagination):
    ordering = '-created_at'
    page_size = 10