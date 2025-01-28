from django.core.paginator import Paginator

# Create your views here.
class PaginationView():
    def __init__(self, object_on_page: int, list_of_objects: list, curent_page: int) -> None:
        if not(curent_page):
            curent_page = 1
        self.paginator = Paginator(list_of_objects, object_on_page)
        self.current_page = self.paginator.page(curent_page)

    def get_pagintaion_context(self):
        return {
            "number_of_pages" : self.paginator.num_pages,
            "current_page": self.current_page.number,
            "has_previuos": self.current_page.has_previous(),
            "has_next": self.current_page.has_next(),
            "previuos_page": self.current_page.number - 1,
            "next_page": self.current_page.number + 1,
            "page_range": self.paginator.page_range,
        }