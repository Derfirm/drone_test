#!/usr/bin/env python
# -*- coding: utf-8 -*-

from some_code.some_meta_test import Message, cached_property
import unittest

class Test(unittest.TestCase):
    
    def test_meta(self):
        msg = Message(type='text', text='text body')
        self.assertEqual(msg.type, 'text')
        self.assertEqual(msg.text, 'text body')

    def test_cache_property(self):
        class Example(object):
            """docstring for Example"""
            def __init__(self, arg):
                super(Example, self).__init__()
                self._arg = arg
        
            @cached_property
            def incr_value(self):
                self._arg += 50
                return self._arg

        new_inst = Example(100)
        self.assertEqual(new_inst.incr_value, 150)
        self.assertEqual(new_inst.incr_value, 150)
        del new_inst.incr_value
        self.assertEqual(new_inst.incr_value, 200)

if __name__ == "__main__":
    unittest.main()
