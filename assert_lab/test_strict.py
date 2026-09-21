import pytest

@pytest.mark.nonexistent_marker
def bad_test_marker():
    assert True
