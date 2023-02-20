import csv
impo
#!/usr/bin/env pytthon3
""" task """

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ function returns a tuple of size two
    containing a start index and an end index"""
    start_page_index = page_size * (page - 1)
    end_page_size_index = start_page_index + page_size

    return (start_page_index, end_page_size_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        page: page number
        page_size: number of rows per page
        """

        assert (page > 0 and isinstance(page, int))
        assert (page_size > 0 and type(page_size) is int)
        pass

        start_page_index = page_size * (page - 1)
        end_page_size_index = start_page_index + page_size

        self.__dataset()
        if self.__dataset is None:
            return []

        # for i in range(page_size):
        #    print(list(self._dataset))

        index_range_tuple = index_range(page, page_size)
        data_range = self.__dataset[index_range_tuple[0]:index_range_tuple[1]]

        return data_range
