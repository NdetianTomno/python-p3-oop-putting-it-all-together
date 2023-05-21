#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = None
        self._page_count = None
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, (str, int)):
            raise ValueError("Title must be a string or integer.")
        self._title = str(value)

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            raise ValueError("Page count must be an integer.")
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
