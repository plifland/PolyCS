import check50

@check50.check()
def exists():
    """PersonalizedHello.java exists"""
    check50.exists("PersonalizedHello.java")

@check50.check(exists)
def test1():
    """handles a 1 word name correctly """
    check50.run("java ./PersonalizedHello.java").stdin("Panther", timeout=10).stdout("Hello, Panther!")

@check50.check(exists)
def test2():
    """handles a name with a space correctly """
    check50.run("java ./PersonalizedHello.java").stdin("Poly Panther", timeout=10).stdout("Hello, Poly Panther!")
