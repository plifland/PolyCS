import check50

@check50.check()
def exists():
    """IsPrime.java exists."""
    check50.exists("IsPrime.java")

@check50.check(exists)
def compiles():
    """IsPrime.java compiles"""
    check50.run("javac IsPrime.java").exit(0)

@check50.check(compiles)
def test2():
    """2 is prime"""
    check50.run("java IsPrime").stdin("2").stdout("true").exit()

@check50.check(compiles)
def test4():
    """4 is not prime"""
    check50.run("java IsPrime").stdin("4").stdout("false").exit()

@check50.check(compiles)
def test13():
    """13 is prime"""
    check50.run("java IsPrime").stdin("13").stdout("true").exit()

@check50.check(compiles)
def test99991():
    """99991 is prime"""
    check50.run("java IsPrime").stdin("99991").stdout("true").exit()

@check50.check(compiles)
def test9998000099():
    """998000099 is not prime"""
    check50.run("java IsPrime").stdin("998000099").stdout("false").exit()

@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("java IsPrime").stdin("-1").reject()

@check50.check(compiles)
def test_reject_one():
    """rejects an input of 1, which can't be prime"""
    check50.run("java IsPrime").stdin("1").reject()

@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("java IsPrime").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty():
    """rejects an empty input of "" """
    check50.run("java IsPrime").stdin("").reject()
