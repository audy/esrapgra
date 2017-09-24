#!/usr/bin/env python3

from esrapgra import esrapgra

def test_that_it_esrapgras():
    res = esrapgra(
            'bleep',
            'bloop',
            some_argument=21,
            another_argument=1000
            )

    assert res == '--some-argument=21 --another-argument=1000 bleep bloop'


def test_kwargs_last():

    res = esrapgra(
            'bleep',
            'bloop',
            some_argument=21,
            another_argument=1000,
            _kwargs_last=False
            )

    assert res == 'bloop bleep --some-argument=21 --another-argument=1000'
