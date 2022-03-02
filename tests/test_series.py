from math_series.series import *

"""
Fibonacci Series  : 0, 1, 1, 2, 3, 5, 8, 13, ...

Lucas Numbers  : 2, 1, 3, 4, 7, 11, 18, 29, ...

test_sum_series : ( if with the dafault ) 0, 1, 1, 2, 3, 5, 8, 13, ...  other wise based on user input value 


"""
def test_Fib():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_Lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_sum_series():
    actual = sum_series(4,4,3)
    expected = 17
    assert actual == expected


def test_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


