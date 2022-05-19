num = int(input("Enter the nth position (>=0) in the series: "))
a = int(input("Enter the 0 position value in the series: ") or "0")
b = int(input("Enter the 1 position value in the series: ") or "1")


# Creating fibonacci function below
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


# Invoke functions and store the value of the nth position in n
i = 0
while i <= num:
    n = fibonacci(i)
    nl = lucas(i)
    i += 1


def sum_series(no, a=0, b=1):
    """Takes in a number n, returns the number in the nth position of the series that starts with
    the specified first two values. For ex"""
    if no == 0:
        return a
    elif no == 1:
        return b
    else:
        return sum_series(no - 1, a, b) + sum_series(no - 2, a, b)


i = 0
while i <= num:
    no = sum_series(i, a, b)
    i += 1

print(sum_series(num, a, b))
