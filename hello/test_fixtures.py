import pytest


# scope="function" -- tear down will be run after each test is executed
# scope="module" -- tear down will be run after all tests are executed
@pytest.fixture(scope="module")
def any_name():
    print("setup")
    yield 5
    print("teardown")


def test_a(any_name):
    print("do something")
    print("assert something")
    assert any_name == 5


def test_b(any_name):
    print("do something")
    print("assert something")
    assert any_name == 5
