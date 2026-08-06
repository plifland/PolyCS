import check50

@check50.check()
def exists():
    """ExtrovertsVsIntroverts.java exists"""
    check50.exists("ExtrovertsVsIntroverts.java")

@check50.check(exists)
def test1000():
    """Serves a dog food ad for someone with 1000 friends"""
    check50.run("java ExtrovertsVsIntroverts.java").stdin("1000", timeout=10).stdout("Dog food ad:.+", regex=True).exit()

@check50.check(exists)
def test501():
    """Serves a dog food ad for someone with 501 friends"""
    check50.run("java ExtrovertsVsIntroverts.java").stdin("501", timeout=10).stdout("Dog food ad:.+", regex=True).exit()

@check50.check(exists)
def test500():
    """Serves a cat food ad for someone with 500 friends"""
    check50.run("java ExtrovertsVsIntroverts.java").stdin("500", timeout=10).stdout("Cat food ad:.+", regex=True).exit()

@check50.check(exists)
def test0():
    """Serves a cat food ad for someone with 0 friends"""
    check50.run("java ExtrovertsVsIntroverts.java").stdin("0", timeout=10).stdout("Cat food ad:.+", regex=True).exit()
