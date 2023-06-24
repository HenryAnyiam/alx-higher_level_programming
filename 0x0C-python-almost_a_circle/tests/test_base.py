#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(89)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')
        self.assertIsInstance(Base.to_json_string([ { 'id': 12 }]), str)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{ "id": 89 }])
        self.assertIsInstance(Base.from_json_string('[{ "id": 89 }]'), list)
