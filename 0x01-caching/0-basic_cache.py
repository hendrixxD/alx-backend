#!/usr/bin/env python3
"""
Basic dictionary
"""

from base_chaching import BaseCaching


class BasicCache(BaseCaching):
    """
    Base class: BaseCaching
    """

    def __init__(self):
        """
        initialize the class using
        __init__ parent class
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        assigns dic self.cache_Data
        the item value for the key
        """
        if key or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        args:
         key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
