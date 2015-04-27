# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.table_value import TableValue


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTableValueEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = TableValue('AS', 'Assignor',
                          'The entitled party who is assigning the rights to a musical work within an agreement')

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('AS', encoded['code'])
        self.assertEqual('Assignor', encoded['name'])
        self.assertEqual('The entitled party who is assigning the rights to a musical work within an agreement',
                         encoded['description'])