import pytest
def test_example():
    assert 1 + 1 == 2
    assert 2 * 2 == 4
    names=["apoorva","pooja","priya"]
    assert "apoorva" in names
    users={"apoorva":1,"pooja":2,"priya":3}
    assert users["apoorva"] == 1
    print("This is a test for example")


def test_string_comparison():
    assert "apoorva" == "apoorva"
    assert "poo" in "apoorva"
    print("This is a test for string comparison")