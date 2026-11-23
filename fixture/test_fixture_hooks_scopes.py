import pytest


@pytest.fixture(scope="module")
def db_connection():
    connection="connected to DB"
    print(f"This is a test for db connection: {connection}")
    yield connection
    connection="disconnected to DB"
    print(f"This is a test for db disconnection: {connection}")


class TestDBConnection:
    def test_db_connection(self, db_connection):
        assert db_connection == "connected to DB"
        print("This is a test for db connection assertion")

    def test_db_connection_another(self, db_connection):
        assert db_connection == "connected to DB"
        print("This is a test for db connection assertion")

class TestDBConnectionTwo:
    def test_db_connection_two(self, db_connection):
        assert db_connection == "connected to DB"
        print("This is a test for db connection assertion")

    def test_db_connection_another_two(self, db_connection):
        assert db_connection == "connected to DB"
        print("This is a test for db connection assertion")