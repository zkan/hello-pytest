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


def test_greeting():
    result = hello.full_output("-g Hey")
    assert result == "Hey, World!"


def test_greeting_long():
    result = hello.full_output("--greeting Hey")
    assert result == "Hey, World!"


def test_name():
    result = hello.full_output("-n Kan")
    assert result == "Hello, Kan!"


def test_name_long():
    result = hello.full_output("--name Kan")
    assert result == "Hello, Kan!"
