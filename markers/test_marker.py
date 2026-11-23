import pytest

@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_marker_example():
    assert 1 + 1 == 2
    assert 2 * 2 == 4
    print("This is a test for marker example")

@pytest.mark.xfail(reason="This test is expected to fail")
def test_marker_failing_example():
    assert 1 + 1 == 3
    print("This is a test for marker example")