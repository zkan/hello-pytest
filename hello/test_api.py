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


@pytest.mark.parametrize("arg_str", [
    "-g Hey",
    "--greeting Hey",
])
def test_greeting(arg_str):
    result = hello.full_output(arg_str)
    assert result == "Hey, World!"


@pytest.mark.parametrize("arg_str", [
    "-n Kan",
    "--nam Kan",
])
def test_name(arg_str):
    result = hello.full_output(arg_str)
    assert result == "Hello, Kan!"
