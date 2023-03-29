import pytest
import app as tested_app

def test_get_hello_endpoint():
    tmp = tested_app.hello()
    assert tmp == "Hello World!1"
