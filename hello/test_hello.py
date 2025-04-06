import hello


def test_hello(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result == "Hello, World!"


def test_comma(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert "," in result


def test_exclamation(capsys):
    hello.main()
    result = capsys.readouterr().out.rstrip()
    assert result.endswith("!")
