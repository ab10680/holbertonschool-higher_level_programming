#!/usr/bin/env python3
"""Defines a CountedIterator that tracks number of items iterated."""

class CountedIterator:
    """Custom iterator that counts how many items have been returned."""

    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        item = next(self._iterator)  # Will raise StopIteration automatically
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items iterated."""
        return self._count

    def __iter__(self):
        return self
