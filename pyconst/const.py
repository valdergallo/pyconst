# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from .slug import slugify as s
from .slug import slugify_attr as s_attr


class PyConstString(str):

    def __new__(cls, label=None, value=None, to_upper=True):
        if not value:
            value = label
        if to_upper:
            value = s(value).upper()
        else:
            value = s(value)
        obj = str.__new__(cls, value)
        obj.label = label
        return obj


class Const(object):

    def __init__(self, *args, **kwargs):
        self.__data = ()
        for value in args:
            self.add(value)

        for label, attr in kwargs.items():
            self.add(label, attr)

    def __set_iter_value(self, iter_value):
        label, attr, value = (None,) * 3
        if len(iter_value) == 1:
            label = iter_value[0]
        elif len(iter_value) == 2:
            label, attr = iter_value
        elif len(iter_value) == 3:
            label, attr, value = iter_value
        elif len(iter_value) > 3:
            attr = iter_value[1]
            value = iter_value[2]
            label = iter_value[0]
        return label, attr, value

    def add(self, label, attr=None, value=None, to_upper=True):
        "Set values in constant"

        if isinstance(label, tuple) or isinstance(label, list):
            label, attr, value = self.__set_iter_value(label)

        if attr is None:
            attr = label

        if value is None:
            value = attr

        self.__data += (PyConstString(label=label, value=value, to_upper=to_upper),)
        # set attribute as slugfiy
        self.__dict__[s_attr(attr)] = self.__data[-1]

    def __getitem__(self, index):
        "Get index item"
        return (self.__data[index], self.__data[index].label)

    def __iter__(self):
        "Lazy return"
        return ((i, i.label) for i in self.__data)

    def __len__(self):
        return len(self.__data)
