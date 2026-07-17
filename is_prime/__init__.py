import check50

@check50.check()
def exists():
    """is_prime.py exists."""
    check50.exists("is_prime.py")

@check50.check(exists)
def test2():
    """2 is prime"""
    check50.run("python3 is_prime.py").stdin("2").stdout("True\n").exit()

@check50.check(exists)
def test4():
    """4 is not prime"""
    check50.run("python3 is_prime.py").stdin("4").stdout("False\n").exit()

@check50.check(exists)
def test13():
    """13 is prime"""
    check50.run("python3 is_prime.py").stdin("13").stdout("True\n").exit()

@check50.check(exists)
def test99991():
    """99991 is prime"""
    check50.run("python3 is_prime.py").stdin("99991").stdout("True\n").exit()

@check50.check(exists)
def test9998000099():
    """9998000099 is not prime"""
    check50.run("python3 is_prime.py").stdin("9998000099").stdout("False\n").exit()

@check50.check(exists)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("python3 is_prime.py").stdin("-1").reject()

@check50.check(exists)
def test_reject_negative():
    """rejects an input of 1, which can't be prime"""
    check50.run("python3 is_prime.py").stdin("1").reject()

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("python3 is_prime.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("python3 is_prime.py").stdin("").reject()
