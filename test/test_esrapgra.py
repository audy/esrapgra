import pytest
from esrapgra import Esrapgra


def test_basic():
    res = Esrapgra().lex_arguments(
        "bleep", "bloop", some_argument=21, another_argument=1000, bool_argument=True
    )

    assert res == [
        "--some-argument=21",
        "--another-argument=1000",
        "--bool-argument",
        "bleep",
        "bloop",
    ]


def test_quote_strings():
    esrapgra = Esrapgra(quote_strings=True)
    assert esrapgra.lex_arguments(test="asdf; * asdf") == ["--test='asdf; * asdf'"]

    esrapgra = Esrapgra(quote_strings=False)
    assert esrapgra.lex_arguments(test="asdf; * asdf") == ["--test=asdf; * asdf"]


@pytest.mark.parametrize("bool_argument_value", [(True), (False)])
def test_bool_argument(bool_argument_value):
    res = Esrapgra().lex_arguments(
        "bleep", "bloop", some_argument=21, another_argument=1000, bool_argument=bool_argument_value
    )

    assert ("--bool-argument" in res) == bool_argument_value


@pytest.mark.parametrize("kwargs_last_value", [(True), (False)])
def test_kwargs_last(kwargs_last_value):
    res = Esrapgra(kwargs_last=kwargs_last_value).lex_arguments(
        "bleep", some_argument=21, another_argument=1000
    )

    if kwargs_last_value:
        assert res[0] == "bleep"
    else:
        assert res[-1] == "bleep"
