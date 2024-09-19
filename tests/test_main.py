'''My Calculator Test'''
from app.main import addition, subtraction

def test_addition():
    '''Addition function'''
    assert addition(1,1) == 2

def test_subtraction():
    assert subtraction(1,1) == 0
