#!/usr/bin/env python3
"""
a simple helper function
"""


def index_range(page, page_size):
    """
    attribute:
        page: page number
        page_size: page size
    """

    # page = int(input('enter a page number: '))
    # page_size = int(input('enter a page size: '))

    start_page_index = page_size * (page - 1)
    end_page_size_index = start_page_index + page_size

    index_range = [start_page_index, end_page_size_index]

    return tuple(index_range)
