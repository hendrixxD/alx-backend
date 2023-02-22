#!/usr/bin/env python3
""" LRU caching module
"""
from base_chaching import BaseCaching


class LRUCache(BaseCaching):
    """class LRU cache"""

    def __init__(self):
        """constructor function"""
        super().__init__()
        self.used = []

    def put(self, key, item):
        """function to put the items"""
        dictlen = len(self.cache_data)
        if key is None or item is None:
            pass
        else:
            if dictlen >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.used[0]}")
                del self.cache_data[self.used[0]]
                del self.used[0]
            if key in self.used:
                del self.used[self.used.index(key)]
            self.used.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """function to get"""
        if key is not None and key in self.cache_data.keys():
            del self.used[self.used.index(key)]
            self.used.append(key)
            return self.cache_data.get(key)
        return None
