#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AttrInit(type):

    def __call__(cls, **kwargs):
        obj = super(AttrInit, cls).__call__()
        for name, value in kwargs.items():
            setattr(obj, name, value)
        return obj


class Message(object):
    __metaclass__ = AttrInit

class cached_property(object):
    """ A property that is only computed once per instance and then replaces
        itself with an ordinary attribute. Deleting the attribute resets the
        property.
        Source: https://github.com/bottlepy/bottle/commit/fa7733e075da0d790d809aa3d2f53071897e6f76
        """

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


class Example(object):
    """docstring for Example"""
    def __init__(self, arg):
        super(Example, self).__init__()
        self._arg = arg
    
    @cached_property
    def incr_value(self):
        self._arg += 50
        return self._arg        

