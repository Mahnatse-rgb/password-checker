import pytest
from password_checker import *

def test_password_is_valid():

    with pytest.raises(Exception):
        assert password_is_valid('') == Exception('password should exist')
        assert password_is_valid('mahnatse') == Exception('password should be longer than than 8 characters')
        assert password_is_valid('CHOUNGMAHNATSE') == Exception('password should have at least one lowercase letter')
        assert password_is_valid('mahnatseisawesome') == Exception('password should have at least one uppercase letter')
        assert password_is_valid('Choung01Mahnatse') == Exception('password should at least have one digit')
        assert password_is_valid('Ch-oung') == Exception('password should have at least one special character')


