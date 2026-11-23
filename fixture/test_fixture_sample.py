import pytest
@pytest.fixture
def user_data():
    user={"name":"apoorva","age":25,"city":"hyderabad"}
    return user


def test_user_name(user_data):
    assert user_data["name"] == "apoorva"
    print("This is a test for user name")