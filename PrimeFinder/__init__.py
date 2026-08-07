import check50

@check50.check()
def exists():
    """PrimeFinder.java exists."""
    check50.exists("PrimeFinder.java")

@check50.check(exists)
def compiles():
    """PrimeFinder.java compiles"""
    check50.run("javac PrimeFinder.java").exit(0)

@check50.check(compiles)
def test1():
    """2 is prime"""
    check50.run("java PrimeFinder").stdin("2").stdout("2").exit()

@check50.check(compiles)
def test2():
    """4 has two smaller primes"""
    check50.run("java PrimeFinder").stdin("4").stdout("2, 3").exit()

@check50.check(compiles)
def test3():
    """13 has 6 smaller primes, including itself"""
    check50.run("java PrimeFinder").stdin("13").stdout("2, 3, 5, 7, 11, 13").exit()

@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("java PrimeFinder").stdin("-1").reject()

@check50.check(compiles)
def test_reject_negative():
    """rejects an input of 1, which can't be prime"""
    check50.run("java PrimeFinder").stdin("1").reject()

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("java PrimeFinder").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("java PrimeFinder").stdin("").reject()
