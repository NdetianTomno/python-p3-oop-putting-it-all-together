#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = None
        self._size = None
        self.brand = brand
        self.size = size
        self.condition = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string.")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("Size must be an integer.")
        self._size = value

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"
