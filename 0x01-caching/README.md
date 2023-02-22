# 0x01. Caching

<b>Parent class</b> <em>BaseCaching</em>
All your classes must inherit from `BaseCaching` defined below:


`#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")`

## <b>Tasks</b>
- 0. Basic dictionary
	0-basic_cache.py
- 1. FIFO caching
	1-fifo_cache.py
- 2. LIFO Caching
	2-lifo_cache.py
- 3. LRU Caching
	3-lru_cache.py
- 4. MRU Caching
	4-mru_cache.py
- 5. LFU Caching
	100-lfu_cache.py
