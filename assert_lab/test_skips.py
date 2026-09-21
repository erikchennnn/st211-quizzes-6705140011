import pytest
import sys

@pytest.mark.skip(reason="Feature not implemented yet")
def test_futture_feature():
    assert False

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_needs_mordern_python():
    assert True