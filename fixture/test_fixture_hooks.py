import pytest

class TestDBConnection:
    def test_db_connection(self, db_connection):
        assert db_connection == "connected to DB"
        print("This is a test for db connection assertion")

    def test_db_connection_another(self, db_connection):
        assert db_connection == "connected to DB"
        print("This is a test for db connection assertion")