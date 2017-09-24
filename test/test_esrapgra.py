#!/usr/bin/env python3

import unittest
from esrapgra import esrapgra

class TestEsrapgra(unittest.TestCase):

    def test_that_it_esrapgras(self):
        res = esrapgra(
                'bleep',
                'bloop',
                some_argument=21,
                another_argument=1000,
                bool_argument=True
                )

        self.assertEqual(
                ['--some-argument=21', '--another-argument=1000', '--bool-argument', 'bleep', 'bloop'],
                res
                )

    def test_that_it_bools_false(self):
        res = esrapgra(
                'bleep',
                'bloop',
                some_argument=21,
                another_argument=1000,
                bool_argument=False
                )

        self.assertEqual(
                ['--some-argument=21', '--another-argument=1000', 'bleep', 'bloop'],
                res
                )

    def test_kwargs_last(self):

        res = esrapgra(
                'bleep',
                'bloop',
                some_argument=21,
                another_argument=1000,
                _kwargs_last=False
                )

        self.assertEqual(
                ['bloop', 'bleep', '--some-argument=21', '--another-argument=1000'],
                res
                )
