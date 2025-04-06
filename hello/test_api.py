import pytest

import hello


def test_hello():
    result = hello.full_output()
    assert result == "Hello, World!"


def test_comma():
    result = hello.full_output()
    assert "," in result


def test_exclamation():
    result = hello.full_output()
    assert result.endswith("!")


def idfn(x):
    return f'"{x}"'


@pytest.mark.parametrize("arg_str, expected", [
    ("-g Hey", "Hey, World!"),
    ("--greeting Hey", "Hey, World!"),
    ("-n Kan", "Hello, Kan!"),
    ("--nam Kan", "Hello, Kan!"),
    ("-g Hey -n Kan", "Hey, Kan!"),
], ids=idfn)
def test_greeting(arg_str, expected):
    result = hello.full_output(arg_str)
    assert result == expected
