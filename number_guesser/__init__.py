import check50

@check50.check()
def exists():
    """number_guesser.py exists"""
    check50.exists("number_guesser.py")

@check50.check(exists)
def test_too_low():
    """Guessing too low on the first guess says 'Too low'"""
    check50.run("python3 number_guesser.py").stdin("0", prompt=True).stdout(".*[Tt]oo low.*", regex=True).kill()

@check50.check(exists)
def test_too_high():
    """Guessing too high on the first guess says 'Too high'"""
    check50.run("python3 number_guesser.py").stdin("11", prompt=True).stdout(".*[Tt]oo high.*", regex=True).kill()

@check50.check(exists)
def test_too_low2():
    """Guessing too low on the second guess says 'Too low'"""
    check50.run("python3 number_guesser.py").stdin("11", prompt=True).stdin("0", prompt=True).stdout(".*[Tt]oo low.*", regex=True).kill()

@check50.check(exists)
def test_too_high2():
    """Guessing too high on the second guess says 'Too high'"""
    check50.run("python3 number_guesser.py").stdin("0", prompt=True).stdin("11", prompt=True).stdout(".*[Tt]oo high.*", regex=True).kill()

@check50.check(exists)
def test_lose():
    """Guessing wrong three times loses"""
    check50.run("python3 number_guesser.py").stdin("0", prompt=True).stdin("0", prompt=True).stdin("0", prompt=True).stdout(".*[Ll]os[et].*", regex=True).exit()
