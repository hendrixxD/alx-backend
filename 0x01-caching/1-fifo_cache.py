#!/usr/bin/env python3
"""
FIFO caching
"""

BaseCaching = __import__('base_chaching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Caching
    """

    def __init__(self):
        """
        constructor function
        """
        super().__init__()

    def put(self, key, item):
        """
        assigns self.cache_data to item
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                self.cache_data.pop(first)
                print(f'DISCARD: {first}')
            self.cache_data[key] = item

    def get(self, key):
        """
        function to get
        """
        if key is None and key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
