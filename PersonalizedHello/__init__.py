import check50

@check50.check()
def exists():
    """PersonalizedHello.java exists"""
    check50.exists("PersonalizedHello.java")

@check50.check(exists)
def compiles():
    """PersonalizedHello.java compiles"""
    check50.run("javac PersonalizedHello.java").exit()

@check50.check(compiles)
def test1():
    """handles a 1 word name correctly """
    check50.run("java ./PersonalizedHello").stdin("Panther").stdout("Hello, Panther!")

@check50.check(compiles)
def test2():
    """handles a name with a space correctly """
    check50.run("java ./PersonalizedHello").stdin("Poly Panther").stdout("Hello, Poly Panther!")
