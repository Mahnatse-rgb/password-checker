import pytest
from password_checker import password_is_ok

def test_password_is_ok():

        assert password_is_ok('') == False
        assert password_is_ok('choung') == False
        assert password_is_ok('MAHNATSECHOUNG') == False
