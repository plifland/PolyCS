import check50

@check50.check()
def exists():
    """luggage_password.py exists."""
    check50.exists("luggage_password.py")

@check50.check(exists)
def test1():
    """flags 12345"""
    check50.run("python3 luggage_password.py").stdin("12345").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test2():
    """flags poly12"""
    check50.run("python3 luggage_password.py").stdin("poly12").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test3():
    """flags 34poly"""
    check50.run("python3 luggage_password.py").stdin("34poly").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test4():
    """flags po67ly"""
    check50.run("python3 luggage_password.py").stdin("po67ly").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test5():
    """passes Poly2006"""
    check50.run("python3 luggage_password.py").stdin("Poly2006").stdout("PASSED\n").exit()

@check50.check(exists)
def test6():
    """flags password"""
    check50.run("python3 luggage_password.py").stdin("password").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test7():
    """flags !password!"""
    check50.run("python3 luggage_password.py").stdin("!password!").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test8():
    """flags PasswoRd"""
    check50.run("python3 luggage_password.py").stdin("PasswoRd").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test9():
    """flags P@$sW0rd!"""
    check50.run("python3 luggage_password.py").stdin("P@$sW0rd!").stdout("FLAGGED\n").exit()

@check50.check(exists)
def test10():
    """passes passwourd"""
    check50.run("python3 luggage_password.py").stdin("passwourd").stdout("PASSED\n").exit()