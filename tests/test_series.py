from math_series.series import *

"""
Fibonacci Series  : 0, 1, 1, 2, 3, 5, 8, 13, ...

Lucas Numbers  : 2, 1, 3, 4, 7, 11, 18, 29, ...

test_sum_series : ( if with the dafault ) 0, 1, 1, 2, 3, 5, 8, 13, ...  other wise based on user input value 


"""
def test_Fib1():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_Fib2():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_Fib3():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_Fib4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_Lucas1():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_Lucas2():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_Lucas3():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_Lucas4():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_sum_series1():
    actual = sum_series(4,4,3)
    expected = 17
    assert actual == expected


def test_sum_series2():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_sum_series3():
    actual = sum_series(3,2,6)
    expected = 14
    assert actual == expected

def test_sum_series4():
    actual = sum_series(6,2,2)
    expected = 26
    assert actual == expected


