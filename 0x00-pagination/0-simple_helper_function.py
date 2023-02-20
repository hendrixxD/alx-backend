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

    page = int(input('enter a page number: '))
    page_size = int(input('enter a page size: '))

    page_index = page_size * (page - 1)
    page_size_index = page_index + page_size

    index_range = [page_index, page_size_index]

    return tuple(index_range)
