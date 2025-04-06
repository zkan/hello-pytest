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
