#!/bin/env python


class dicto(dict):
    """dict subclass to allow dotted notation"""

    def __init__(self, *args, **kwargs):
        super(dicto, self).__init__(*args, **kwargs)
        self.__dict__ = self
        self.init()

    def init(self):
        """used for subclassing to assign initial attributes"""
        pass

    def export(self):
        """exports all attributes to a true dict
        this allows you to pass the object to a
        function or class that has strict type checking
        """
        d = dict()
        for k, v in self.items():
            d[k] = v
        return d

    def lowercasekeys(self):
        """converts all keys to lowercase"""
        for k, v in self.items():
            null = self.pop(k)
            k = k.lower()
            self[k] = v
        return self
