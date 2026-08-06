import check50

@check50.check()
def exists():
    """ExtrovertsVsIntroverts.java exists"""
    check50.exists("ExtrovertsVsIntroverts.java")

@check50.check(exists)
def compiles():
    """ExtrovertsVsIntroverts.java compiles"""
    check50.run("javac ExtrovertsVsIntroverts.java").exit()

@check50.check(compiles)
def test1000():
    """Serves a dog food ad for someone with 1000 friends"""
    check50.run("java ExtrovertsVsIntroverts").stdin("1000").stdout("^Dog food ad:.+", "Dog food ad:").exit()

@check50.check(compiles)
def test501():
    """Serves a dog food ad for someone with 501 friends"""
    check50.run("java ExtrovertsVsIntroverts").stdin("501").stdout("^Dog food ad:.+", "Dog food ad:").exit()

@check50.check(compiles)
def test500():
    """Serves a cat food ad for someone with 500 friends"""
    check50.run("java ExtrovertsVsIntroverts").stdin("500").stdout("^Cat food ad:.+", "Cat food ad:").exit()

@check50.check(compiles)
def test0():
    """Serves a cat food ad for someone with 0 friends"""
    check50.run("java ExtrovertsVsIntroverts").stdin("0").stdout("^Cat food ad:.+", "Cat food ad:").exit()
