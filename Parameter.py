import pytest
from Dictionary import Dictionary

@pytest.fixture(scope="function", params=[
        (['а','б','в','г'], [1,2,3,4,5], {'а': 1, 'б': 2, 'в': 3, 'г': 4}),
        ([], [], {}),
        (['а','б','в'], [1,2,3,4,5], {'а': 1, 'б': 2, 'в': 3}),
        (['а','б','в'], [1,2], {'а': 1, 'б': 2, 'в': None})],
        ids = ['test1','test2','test3','test4'])

def test(request):
    return request.param

def the_test(test):
    (key,value,expected_result) = test
    calculated_result = Dictionary(key,value)
    print("input: {0}, output: {1}, expected: {2}".format([key,value], calculated_result, expected_result))
    assert Dictionary(key,value) == expected_result