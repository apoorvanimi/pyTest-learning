
import time

import pytest


@pytest.fixture(scope="module")
def db_connection():
    connection="connected to DB"
    print(f"This is a test for db connection: {connection}")
    time.sleep(2)
    yield connection
    connection="disconnected to DB"
    print(f"This is a test for db disconnection: {connection}")