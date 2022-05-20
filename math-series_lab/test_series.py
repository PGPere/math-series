from series import fibonacci, lucas, sum_series


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected


def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_nine():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_sum_series_3_default():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_sum_series_five_two_one():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected


def test_sum_series_three_two_three():
    actual = sum_series(8, 2, 3)
    expected = 89
    assert actual == expected
