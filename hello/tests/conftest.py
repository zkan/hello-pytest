import pytest

import hello


@pytest.fixture(scope="module")
def hello_result():
    """
    Returns full output with no cli args
    """
    return hello.full_output()
