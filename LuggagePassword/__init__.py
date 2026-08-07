import check50

@check50.check()
def exists():
    """LuggagePassword.java exists."""
    check50.exists("LuggagePassword.java")

@check50.check(exists)
def compiles():
    """LuggagePassword.java compiles"""
    check50.run("javac LuggagePassword.java").exit(0)

@check50.check(compiles)
def test1():
    """flags 12345"""
    check50.run("java LuggagePassword").stdin("12345").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test2():
    """flags poly12"""
    check50.run("java LuggagePassword").stdin("poly12").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test3():
    """flags 34poly"""
    check50.run("java LuggagePassword").stdin("34poly").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test4():
    """flags po67ly"""
    check50.run("java LuggagePassword").stdin("po67ly").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test5():
    """passes Poly2006"""
    check50.run("java LuggagePassword").stdin("Poly2006").stdout("PASSED\n").exit()

@check50.check(compiles)
def test6():
    """flags password"""
    check50.run("java LuggagePassword").stdin("password").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test7():
    """flags !password!"""
    check50.run("java LuggagePassword").stdin("!password!").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test8():
    """flags PasswoRd"""
    check50.run("java LuggagePassword").stdin("PasswoRd").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test9():
    """flags P@$sW0rd!"""
    check50.run("java LuggagePassword").stdin("P@$sW0rd!").stdout("FLAGGED\n").exit()

@check50.check(compiles)
def test10():
    """passes passwourd"""
    check50.run("java LuggagePassword").stdin("passwourd").stdout("PASSED\n").exit()