import pytest

@pytest.mark.api
@pytest.mark.ui
def test_a():
    assert 1 == 2

class Test:

    @pytest.mark.ui
    def test_b(self):
        pass