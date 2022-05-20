

# Creating Fibonacci function below
def fibonacci(n):
    """Takes in a number n, returns the number in the nth position of the Fibonacci series.
       The first 8 numbers of the Fibonacci series are 0, 1, 1, 2, 3, 5, 8, 13, ... """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Creating Lucas function below
def lucas(nl):
    """Takes in a number n, returns the number in the nth position of the Lucas series.
    The first 8 numbers of the Lucas series are 2, 1, 3, 4, 7, 11, 18, 29, ..."""
    if nl == 0:
        return 2
    elif nl == 1:
        return nl
    else:
        return lucas(nl - 1) + lucas(nl - 2)


def sum_series(no, a=0, b=1):
    """Takes in a number n, returns the number in the nth position of the series that starts with
    the specified first two values. """
    if no == 0:
        return a
    elif no == 1:
        return b
    else:
        return sum_series(no - 1, a, b) + sum_series(no - 2, a, b)
