import pytest

import hello


@pytest.fixture(scope="module")
def hello_result():
    return hello.full_output()


def test_hello(hello_result):
    assert hello_result == "Hello, World!"


def test_comma(hello_result):
    assert "," in hello_result


def test_exclamation(hello_result):
    assert hello_result.endswith("!")


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
