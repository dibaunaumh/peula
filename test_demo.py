import doctest

def factorial(n):
    """
    Returns the factorial of n
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(5)
120
>>> factorial(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000L
    """
    return n*factorial(n-1) if n > 1 else 1


if __name__ == "__main__":
    doctest.testmod()