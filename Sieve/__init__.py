import check50

@check50.check()
def exists():
    """Sieve.java exists."""
    check50.exists("Sieve.java")

@check50.check(exists)
def compiles():
    """Sieve.java compiles"""
    check50.run("javac Sieve.java").exit(0)

@check50.check(compiles)
def test2():
    """2 is prime"""
    check50.run("java Sieve").stdin("2").stdout("2").exit()

@check50.check(compiles)
def test4():
    """4 has two smaller primes"""
    check50.run("java Sieve").stdin("4").stdout("2, 3").exit()

@check50.check(compiles)
def test13():
    """13 has 6 smaller primes, including itself"""
    check50.run("java Sieve").stdin("13").stdout("2, 3, 5, 7, 11, 13").exit()

@check50.check(compiles)
def test100000():
    """100,000 primes is fast enough to finish"""
    check50.run("java Sieve").stdin("100000").exit()

@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("java Sieve").stdin("-1").reject()

@check50.check(compiles)
def test_reject_negative():
    """rejects an input of 1, which can't be prime"""
    check50.run("java Sieve").stdin("1").reject()

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("java Sieve").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("java Sieve").stdin("").reject()
