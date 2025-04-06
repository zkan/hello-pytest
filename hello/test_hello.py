import hello


def test_hello():
    result = hello.main()
    assert result == "Hello, World!"


def test_comma():
    result = hello.main()
    assert "," in result


def test_exclamation():
    result = hello.main()
    assert result.endswith("!")
