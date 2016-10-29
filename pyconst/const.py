# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from .slug import slugify as s


class PyConstString(str):
    def __new__(cls, attr, label):
        obj = str.__new__(cls, s(attr))
        obj.label = label
        return obj


class PyConst(object):

    def __init__(self, *args, **kwargs):
        self.__data = ()
        for value in args:
            self.add(value)

        for label, attr in kwargs.items():
            self.add(label, attr)

    def add(self, label, attr=None):
        "Set values in constant"

        if isinstance(label, tuple) or isinstance(label, list):
            label = label[0]
            try:
                atrr = label[1]
            except IndexError:
                pass

        if not attr:
            attr = label

        self.__data += (PyConstString(attr, label),)
        self.__dict__[s(attr)] = self.__data[-1]

    def __getitem__(self, index):
        "Get index item"
        return (self.__data[index], self.__data[index].label)

    def __iter__(self):
        "Lazy return"
        return ((i, i.label) for i in self.__data)

    def __len__(self):
        return len(self.__data)