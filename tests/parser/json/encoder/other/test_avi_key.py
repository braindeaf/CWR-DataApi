# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.other import AVIKey


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAVIKeyEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = AVIKey(1, 2)

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual(1, encoded['society_code'])
        self.assertEqual(2, encoded['av_number'])