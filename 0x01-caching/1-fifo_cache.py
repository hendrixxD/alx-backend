#!/usr/bin/env python3
"""
FIFO caching
"""

BaseCache = __import__('0-basic_cache').BaseCache


class FIFOCache(BaseCache):
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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.cache_data.popitem()
                print(f'DISCARD: {last[0]}')
            self.cache_data[key] = item

    def get(self, key):
        """
        function to get
        """
        if key is None and key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
