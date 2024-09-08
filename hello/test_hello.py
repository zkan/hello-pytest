def some_func():
    return "Hello, World!"


def test_hello():
    result = some_func()
    assert result == "Hello, World!"


def test_comma():
    result = some_func()
    assert "," in result


def test_exclamation():
    result = some_func()
    assert result.endswith("!")
