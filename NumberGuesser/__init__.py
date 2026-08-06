import check50

@check50.check()
def exists():
    """NumberGuesser exists"""
    check50.exists("NumberGuesser.java")

@check50.check(exists)
def compiles():
    """NumberGuesser.java compiles"""
    check50.run("javac NumberGuesser.java").exit()

@check50.check(compiles)
def test_too_low():
    """Guessing too low on the first guess says 'Too low'"""
    check50.run("java NumberGuesser").stdin("0").stdout(".*[Tt]oo low.*").kill()

@check50.check(compiles)
def test_too_high():
    """Guessing too high on the first guess says 'Too high'"""
    check50.run("java NumberGuesser").stdin("11").stdout(".*[Tt]oo high.*").kill()

@check50.check(compiles)
def test_too_low2():
    """Guessing too low on the second guess says 'Too low'"""
    check50.run("java NumberGuesser").stdin("11").stdin("0").stdout(".*[Tt]oo low.*").kill()

@check50.check(compiles)
def test_too_high2():
    """Guessing too high on the second guess says 'Too high'"""
    check50.run("java NumberGuesser").stdin("0").stdin("11").stdout(".*[Tt]oo high.*").kill()

@check50.check(compiles)
def test_lose():
    """Guessing wrong three times loses"""
    check50.run("java NumberGuesser").stdin("0").stdin("0").stdin("0").stdout(".*[Ll]os[et].*").exit()
