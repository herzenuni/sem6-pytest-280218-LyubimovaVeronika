from Dictionary import Dictionary
import hypothesis.strategies as st
from hypothesis import given

@given(st.lists(st.integers()),st.lists(st.integers()))
def testDictionary(a,b):
    result = Dictionary(a, b)
    expected = expectedResult(a,b)
    assert(result == expected)

def expectedResult(keys,values):
    res = {}
    border = len(values)

    for i in range(len(keys)):
        if (i >= border):
            res.update({keys[i]: None})
        else:
            res.update({keys[i]: values[i]})

    return res

if __name__ == '__main__':
    testDictionary()